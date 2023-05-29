from django.contrib.sessions.middleware import SessionMiddleware


def set_session_middleware(request):
    middleware = SessionMiddleware(get_response=lambda r: None)
    middleware.process_request(request)
    return request

  

def get_test_view_response(view, request):
    response = view.as_view()(
        set_session_middleware(request)
    )
    return response