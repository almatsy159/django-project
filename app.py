
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

def app(environ=None, start_response=None):
    """Simplest possible application object"""
    if environ == None:
        environ = {}
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    print(environ,start_response)
    default = v.index("./",{"vars":{"name":"gaetan"}})
    default = default.encode("utf-8")
    start_response(status, response_headers)
    print(start_response)
    #return iter([data])
    return iter[default]