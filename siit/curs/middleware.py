def simple_middleware(get_response):
    # One-time configuration and initialization.
    print("Salut")
    def middleware(request):
        if "view_count" not in request.session:
            request.session["view_count"] = 0
        else:
            request.session["view_count"] +=1
        request.test = True
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
    return middleware