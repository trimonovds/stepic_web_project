def app(environ, start_response):
    """Simplest possible application object"""
    qs = environ.get('QUERY_STRING')
    parsed_qs = [x + '\n' for x in qs.split('&')]
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain')
    ]
    start_response(status, response_headers)
    return parsed_qs