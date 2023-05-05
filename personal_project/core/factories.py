from django.contrib.sessions.middleware import SessionMiddleware


def set_session_middleware(request):
    middleware = SessionMiddleware(get_response=lambda r: None)
    middleware.process_request(request)
    return request