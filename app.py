
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
# just a comment

import doc.views as v

default = "index"

def app(environ, start_response):
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    print(environ,start_response)
    default = v.index("./",{"vars":{"name":"gaetan"}})
    print(default)
    start_response(status, response_headers)
    print(start_response)
    #return iter([data])
    return default