import os
import requests

# send a post request to django api app (port 8000 /files) with all files contained in a dir

"""
class File:
    def __init__(self,name="noName",ext=".txt",path="./",args=""):
        
        self.name = name
        self.ext = ext
        self.path = path
        self.args = args
        self.url = self.path + self.name + self.ext + self.args
        
    def read_file(self):
        res = ""
        print(f"looking for {self.url}")
        try:
            with open(self.url,"r") as f:
                for i in f.readlines():
                    res += i
                #res = f.readlines()
        except:
            res = "error not found"
            
        finally:
            return res
"""    
class Pre_File:
    def __init__(self,name="noName",ext=".txt",path="doc/static/api/",args="",type="text"):
        
        self.name = name
        self.ext = ext
        self.path = path
        self.args = args
        self.url = self.path + self.name + self.ext + self.args
        self.content = ""
        print(self.url)
        self.read_file()
        
    def read_file(self):
        res = ""
        print(f"looking for {self.url}")
        try:
            with open(self.url,"r",encoding='utf-8') as f:
                for i in f.readlines():
                    res += i
                #res = f.readlines()
            print("found !")
        except:
            print("not found")
            res = "error not found"
            
        finally:
            self.content = res
            return res

#print(os.listdir())

#print(os.getcwd())

#print(os.listdir())
#print(os.getcwd())
#css_lambda = Pre_File("style",".css","doc/static/")
#print(css_lambda.read_file())


def post_file(data=None,name="",destination="http://127.0.0.1:8000/"):
    if data != None:
        url = destination + name + "/"
        print(f"send to {url} : {data}")
        response = requests.post(url,json=data)
        print(response)
    return response


def mk_json(name,data):
    file_name = f"{name}.json"
    res = {file_name:data}
    with open(file_name,"w+") as f:
        f.write(str(res))
    print(f"writed : {res}")
    

### here sending all prog of doc/static/file_api

# this return a 403 (post)
# doesn't work because of "" '' game ...
print(os.getcwd())
my_data = {}
"""
my_path= "doc/static/api/"
print(os.listdir(my_path))
for f in os.listdir(my_path):
    k = Pre_File(f,"",my_path)
    my_data[f"{k.name}.{k.ext}"] = k.content
    #post_file(my_data,"files")    
"""
mk_json("program",my_data)