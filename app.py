import os
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
print("in app.py")
default = "index"

def app(start_response,environ):
    print("in app")
    """Simplest possible application object"""
    #print(start_response,environ)
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-Length', str(len(data)))
    ]
    #print(environ,start_response)
    default = v.index("./",{"vars":{"name":"gaetan"}})
    default = default.encode("utf-8")
    start_response(status, response_headers)
    #print(res)
    #return iter([data])
    return iter[default]
    #return start_response