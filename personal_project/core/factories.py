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


class TestUser:
    
    create_form_data = {
        'email': 'unittest@test.com',
        'password1': '123qaz123',
        'first_name': 'unittest',
        'middle_name': 'unittest',
        'last_name': 'unittest',
        'document': '123456789',
        'phone': '123456789',
        'street': 'unittest',
        'number': '123',
        'city': 'unittest',
        'state': 'unittest',
        'country': 'unittest',
        'gender': 'unittest',
        'birthday': '1990-01-01',
    }
    
    update_form_data = {
        'first_name': 'unittest2',
        'middle_name': 'unittest2',
        'last_name': 'unittest2',
        'document': '12345678',
        'phone': '123456789',
        'street': 'unittest2',
        'number': '123',
        'city': 'unittest2',
        'state': 'unittest2',
        'country': 'unittest2',
        'gender': 'unittest2',
        'birthday': '1990-01-01',
    }