import json
from parsel import Selector

def process_request_body(selector, doc_base_path, examples_doc_path, debug=False):
    #
    # req body params
    #

    request_body = {}

    if selector.xpath(f"{doc_base_path}/h3[1]/text()").get() == "Request body":
        # Get the next div after the "Request body" heading
        next_div = selector.xpath(f"{doc_base_path}/h3[1]/following-sibling::div[1]")
        
        # Check if the next div contains text
        request_body_desc = None
        contains_text = bool(next_div.xpath("text()").get())
        if contains_text:
            # Extract and clean the request body description
            request_body_desc = next_div.xpath("text()").get()
            if request_body_desc:
                request_body_desc = request_body_desc.replace("\n", " ").strip()
                print(f"request body description: {request_body_desc}") if debug else None
                request_body["description"] = request_body_desc
            
            req_body_props_xpath = next_div.xpath('following-sibling::*')

        else:
            # If no text, assume the next div contains parameters
            req_body_props_xpath = next_div

        req_body_props_divs = req_body_props_xpath.get()
        req_body_selector = Selector(text=req_body_props_divs)

        # scalar props
        names = req_body_selector.xpath("//body/div/div/div/a/span/code/text()").getall()
        types = req_body_selector.xpath("//body/div/div/div/a/following-sibling::span/text()").getall()
        descriptions = req_body_selector.xpath("//body/div/div[.//code]/div[last()]/div/text()").getall()

        # Extend descriptions list to match length of names, padding with None
        while len(descriptions) < len(names):
            descriptions.append(None)

        scalar_props = list(zip(names, types, descriptions))

        # complex props
        complex_names = req_body_selector.xpath("//body/div/div/div/div/div/a/span/code/text()").getall()
        complex_types = req_body_selector.xpath("//body/div/div/div/div/div/a/following-sibling::span/text()").getall()
        complex_props = [(name, type_, None) for name, type_ in zip(complex_names, complex_types)]

        # Merge both lists
        all_props = scalar_props + complex_props
        print(f"number of request body props: {len(all_props)}") if debug else None
        print(f"request body props: {all_props}") if debug else None

        # examples
        if selector.xpath(f"{examples_doc_path}/div[1]/h1/text()").get() == "Request samples":
            # we have examples!
            code_block = selector.xpath(f"{examples_doc_path}/div[1]/div/div[2]/div/div[1]/div/pre//text()").getall()
            code_text = ''.join(code_block)
        else:
            raise ValueError(f"No requestBody examples found")

        properties = {}
        for name, type_, description in all_props:
            prop = {
                "type": type_ if type_ != "int64" else "integer",  # OpenAPI uses integer, not int64
                "format": "int64" if type_ == "int64" else None,
            }
            if description:
                prop["description"] = description
            
            # Remove None values
            prop = {k: v for k, v in prop.items() if v is not None}
            
            properties[name] = prop

        request_body = {
            "required": True,
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": properties,
                        "example": json.loads(code_text)
                    }
                }
            }
        }    
        if request_body_desc:
            request_body["description"] = request_body_desc

    return request_body