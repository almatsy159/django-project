
"""
class App:
    pass

def create_app():
    app = App()
    return app

def app(a,b):
    print(f"{a},{b}")
    data = b"hello world !"
    return data

"""

def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])