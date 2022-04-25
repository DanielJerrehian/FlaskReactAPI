def replace_empty_strings_with_none(request):
    for key, value in request.items():
            if value == "":
                request[key] = None
    return request