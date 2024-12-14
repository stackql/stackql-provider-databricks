from parsel import Selector

error_codes_set = set()

def process_responses(selector, doc_base_path, debug=False):
    global error_codes_set
    responses = {}
    
    # doc_base_path = "/html/body/div[1]/div/div[2]/div/div[2]/div[3]/article/div/div[1]"

    responses_header_ix = 0
    if selector.xpath(f"{doc_base_path}/h3[2]/text()").get() == "Responses":
        responses_header_ix = 2
    elif selector.xpath(f"{doc_base_path}/h3[3]/text()").get() == "Responses":
        responses_header_ix = 3

    # Get the first div sibling after our Responses h3
    h3_elem = f"h3[{responses_header_ix}]" if responses_header_ix > 0 else "h3"
    response_xpath = f"{doc_base_path}/{h3_elem}/following-sibling::div[1]"
    response_code = selector.xpath(f"{response_xpath}/div[1]/div/strong/text()").get()[0:3]
    response_desc = selector.xpath(f"{response_xpath}/div[1]/div/span[2]/text()").get()

    print(f"response_code: {response_code}") if debug else None
    if response_code:
        if response_desc:
            response_obj = { "description": response_desc.replace('\n', ' ').strip() if response_desc else None }
        else:
            response_obj = {}
        responses[response_code] = response_obj

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
   
        # Write codes to file
        with open('error_codes.txt', 'a') as f:
            for code in error_codes:
                f.write(f"{code}\n")
    
    # Get all response blocks
    # response_blocks = responses_div.xpath(".//div[contains(@aria-expanded, 'true') or contains(@aria-expanded, 'false')]")
    
    # for block in response_blocks:
    #     # Get response code - clean non-printable chars
    #     code_raw = block.xpath(".//strong/text()").get()
    #     if code_raw:
    #         code = ''.join(c for c in code_raw if c.isprintable()).strip()
            
    #         # Get description if it exists
    #         desc = block.xpath(".//span[2]/text()").get()
            
    #         # Find the response properties div - look within the block
    #         props_div = block.xpath(".//div[2]/div")  # Changed this line
    #         if props_div:
    #             props_div_text = props_div.get()
    #             if props_div_text:  # Add null check
    #                 # Skip if first div is just text (description repeat)
    #                 first_div = props_div.xpath("string(.)").get()
    #                 if first_div and not first_div.strip().startswith('<'):
    #                     props_div = props_div.xpath("following-sibling::div")
    #                     props_div_text = props_div.get()

    #                 if props_div_text:  # Another null check after possible reassignment
    #                     # Process properties similar to request body
    #                     props_selector = Selector(text=props_div_text)
                        
    #                     # Get scalar properties
    #                     names = props_selector.xpath("//body/div/div/div/a/span/code/text()").getall()
    #                     types = props_selector.xpath("//body/div/div/div/a/following-sibling::span/text()").getall()
    #                     descriptions = props_selector.xpath("//body/div/div[.//code]/div[last()]/div/text()").getall()

    #                     # Extend descriptions list to match length of names
    #                     while len(descriptions) < len(names):
    #                         descriptions.append(None)

    #                     scalar_props = list(zip(names, types, descriptions))

    #                     # Get complex properties (arrays/objects)
    #                     complex_names = props_selector.xpath("//body/div/div/div/div/div/a/span/code/text()").getall()
    #                     complex_types = props_selector.xpath("//body/div/div/div/div/div/a/following-sibling::span/text()").getall()
    #                     complex_props = [(name, type_, None) for name, type_ in zip(complex_names, complex_types)]

    #                     # Combine properties
    #                     all_props = scalar_props + complex_props

    #                     # Build response schema
    #                     properties = {}
    #                     for name, type_, description in all_props:
    #                         prop = {
    #                             "type": type_ if type_ != "int64" else "integer",
    #                             "format": "int64" if type_ == "int64" else None,
    #                         }
    #                         if description:
    #                             prop["description"] = description
                            
    #                         # Remove None values
    #                         prop = {k: v for k, v in prop.items() if v is not None}
    #                         properties[name] = prop

    #                     # Build response object
    #                     response_obj = {
    #                         "content": {
    #                             "application/json": {
    #                                 "schema": {
    #                                     "type": "object",
    #                                     "properties": properties
    #                                 }
    #                             }
    #                         }
    #                     }
    #                     if desc:
    #                         response_obj["description"] = desc.strip()
                        
    #                     responses[code] = response_obj
    
    return responses