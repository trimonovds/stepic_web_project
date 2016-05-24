def wsgi_application(environ, start_response):
    # business logic
    status = '200 OK'
    headers = [
        ('Content-type', 'text/plain')
    ]
    body = 'Hello, world'
    start_response(status, headers)
    return [ body ]