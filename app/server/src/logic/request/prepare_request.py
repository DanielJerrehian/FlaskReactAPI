def prepare_request(request):
    req = {key: None if value is "" else value for (key, value) in request.items()}
    return req