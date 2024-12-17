def process_parameters(selector, doc_base_path, debug=False):
    params = []

    # default index values
    path_params_ix = 0
    query_params_ix = 0

    #
    # path params
    #

    # Find the index of the <div> containing the <h3> with text "Path parameters"
    path_params_ix = int(float(selector.xpath(
        f"count({doc_base_path}/*[self::div and .//h3[text()='Path parameters']]/preceding-sibling::div)"
    ).get()))
    if path_params_ix > 0:
        path_params_ix += 1

    # has path params?
    if path_params_ix > 0:
        direct_divs = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/*[name()=\"div\"]")
        for idx, div in enumerate(direct_divs):
            param = {}
            param["name"] = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[1]/a/span[2]/code/text()").get()
            if selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[1]/span[1]/text()").get() == "required":
                param["required"] = True
            type_desc = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[1]/span[2]/text()").get()
            # param_desc = selector.xpath(f"{doc_base_path}/div[{path_params_ix}]/div/div[{idx+1}]/div[3]/div/text()").get()
            # if param_desc:
            #     param_desc.replace("\n", " ").strip()
            # if param_desc and type_desc:
            #     param["description"] = f"({type_desc}) {param_desc}" 
            # elif param_desc:
            #     param["description"] = param_desc
            if type_desc:
                param["description"] = f"{type_desc}"
            param["in"] = "path"
            params.append(param)

    #
    # query params
    #
    
    query_params_ix = int(float(selector.xpath(
        f"count({doc_base_path}/*[self::div and .//h3[text()='Query parameters']]/preceding-sibling::div)"
    ).get()))
    if query_params_ix > 0:
        query_params_ix += 1

    if query_params_ix > 0:
        direct_divs = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/*[name()=\"div\"]")
        for idx, div in enumerate(direct_divs):
            param = {}
            param["name"] = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[1]/a/span[2]/code/text()").get()
            if selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[1]/span[1]/text()").get() == "required":
                param["required"] = True
            type_desc = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[1]/span[2]/text()").get()
            # param_desc = selector.xpath(f"{doc_base_path}/div[{query_params_ix}]/div/div[{idx+1}]/div[3]/div/text()").get()
            # if param_desc:
            #     param_desc = param_desc.replace("\n", " ").strip()
            # if param_desc and type_desc:
            #     param["description"] = f"({type_desc}) {param_desc}"
            # elif param_desc:
            #     param["description"] = param_desc
            if type_desc:
                param["description"] = f"{type_desc}"
            param["in"] = "query"
            params.append(param)  

    return params  