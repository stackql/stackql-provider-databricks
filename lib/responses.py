from parsel import Selector
import json

error_code_descriptions = {
    "400": "Request is invalid or malformed.",
    "401": "The request does not have valid authentication credentials for the operation.",
    "403": "Caller does not have permission to execute the specified operation.",
    "404": "Operation was performed on a resource that does not exist.",
    "409": "Request was rejected due a conflict with an existing resource.",
    "429": "Operation is rejected due to throttling, e.g. some resource has been exhausted, per-user quota.",
    "499": "Operation was canceled by the caller.",
    "500": "Internal error.",
    "501": "Operation is not implemented or is not supported/enabled in this service.",
    "503": "Service is currently unavailable.",
    "504": "Deadline expired before the operation could complete.",
    "509": "An external service is unavailable temporarily as it is being updated."
}

def process_responses(selector, doc_base_path, examples_doc_path, hasRespData, debug=False):
    responses = {}

    # Find h3 element containing exactly "Responses"
    responses_h3 = selector.xpath(f"{doc_base_path}//h3[text()='Responses']")
    
    if responses_h3:
        # Get the response div xpath string for later use
        response_xpath = f"{doc_base_path}//h3[text()='Responses']/following-sibling::div[1]"
        # Now work with the div that follows the h3
        response_div = responses_h3.xpath("following-sibling::div[1]")
        response_code = response_div.xpath("div[1]/div/strong/text()").get()[0:3]
        response_desc = response_div.xpath("div[1]/div/span[2]/text()").get()
    else:
        raise ValueError("Could not find Responses h3 element")

    print(f"response_code: {response_code}") if debug else None
    if response_code:
        if response_desc:
            response_obj = { "description": response_desc.replace('\n', ' ').strip() if response_desc else None }
        else:
            response_obj = {}
        responses[response_code] = response_obj
    else:
        raise ValueError("Could not find response code")

    if hasRespData:
        resp_example = get_response_example(selector, examples_doc_path, response_code, debug)
        if not isinstance(resp_example, (dict, list)):
            print(f"resp_example: {resp_example}") if debug else None
            raise ValueError(f"Response example must be a dictionary or array, got: {type(resp_example)}")
        else:
            print(f"resp_example: {json.dumps(resp_example, indent=2)}") if debug else None    

        # derive the schema from the example
        resp_schema = example_to_json_schema(resp_example)
        print(f"resp_example schema: {json.dumps(resp_schema, indent=2)}") if debug else None

        responses[response_code]["content"] = {
            "application/json": {
                "schema": resp_schema
            }
        }

    #
    # error responses
    #
    err_response_xpath = f"{response_xpath}/following-sibling::div[1]/following-sibling::div[1]"
    err_resp_data = selector.xpath(f"{err_response_xpath}/div[1]/div/text()").get()

    if err_resp_data:
        print(f"err_resp_data: {err_resp_data}") if debug else None
        # Split after "codes:" and get everything after that
        codes_part = err_resp_data.split("codes:")[-1]
        # Split by comma, strip whitespace and any periods
        error_codes = [code.strip().rstrip('.') for code in codes_part.split(',')]
        print(f"error codes: {error_codes}") if debug else None   
        if len(error_codes) == 0:
            raise ValueError("No error codes found")
        for code in error_codes:
            if code in error_code_descriptions:
                err_response_obj = { "description": error_code_descriptions[code] }
            else:
                raise ValueError(f"Uknown HTTP response code: {code}")
            responses[code] = err_response_obj

    return responses

def get_response_example(selector, examples_doc_path, response_code, debug=False):
    # Find 'Response samples' h1 element
    response_samples = selector.xpath(f"{examples_doc_path}//h1[text()='Response samples']")
   
    if not response_samples:
        print("No response samples section found") if debug else None
        return None

    # Get tabs from the next div 
    response_tabs_xpath = f"{examples_doc_path}//h1[text()='Response samples']/following-sibling::div[1]//div[@role='tab']"
    tabs = selector.xpath(response_tabs_xpath)
  
    #
    # test: there should be 0 or 1 response sample tabs
    #
    if len(tabs) == 0:
        print("No response sample tabs found") if debug else None
        return None
    elif len(tabs) > 1:
        raise ValueError(f"Expected 1 response sample tab, found {len(tabs)}")

    discovered_response_code = tabs[0].xpath('.//text()').get()

    #
    # test: response code should match the response code in the tab in examples
    #
    if discovered_response_code:
        if discovered_response_code != response_code:
            raise ValueError(f"Expected response code {response_code}, found {discovered_response_code}")
    else:
        raise ValueError("Could not find response code in tab")

    # Get the response example from the pre element
    example_xpath = f"{examples_doc_path}//h1[text()='Response samples']/following-sibling::div[1]//pre//text()"
    example_text = selector.xpath(example_xpath).getall()
   
    if example_text:
        # Join all text pieces and parse as JSON
        try:
            example_json = json.loads(''.join(example_text))
            return example_json
        except json.JSONDecodeError:
            raise ValueError("Could not parse response example as JSON")
    else:
        raise ValueError("Could not find response example")

def example_to_json_schema(example):
    """Convert a JSON example into a JSON schema"""
    
    def _get_type(value):
        """Helper function to get the type of a value"""
        if isinstance(value, dict):
            return "object"
        elif isinstance(value, list):
            return "array"
        elif isinstance(value, bool):
            return "boolean"
        elif isinstance(value, int):
            return "integer"
        elif isinstance(value, float):
            return "number"
        elif value is None:
            return "null"
        else:
            return "string"

    def _process_value(value):
        """Recursively process a value to build schema"""
        value_type = _get_type(value)
        
        if value_type == "object":
            return {
                "type": "object",
                "properties": {
                    k: _process_value(v) for k, v in value.items()
                }
            }
        elif value_type == "array":
            if not value:  # Empty array
                return {
                    "type": "array",
                    "items": {}
                }
            # Get schema of first item as representative
            return {
                "type": "array",
                "items": _process_value(value[0])
            }
        else:
            return {"type": value_type}

    return _process_value(example)