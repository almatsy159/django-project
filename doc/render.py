import sys

# is a pipe through a python file formating the output in json for example
# need to write input and ooutput fonction ! 
def main(args):
    
    name = args[0]
    res = {"name":name}
    
    args = args[1:]
    if len(args) != 0 :
        #for i in args:
        file = args[0]
        args = args[1:]
        res["input"] = format_input(file,args)
        to_exec = ""
        if file :
            
            print(file)
            with open(file,"r+") as f:
                for l in f.readlines:
                    to_exec+=str(l)
                print(to_exec)
        res["output"] = exec(to_exec)
        # tmp ?
        res["output"] = format_output(res["output"])
            #exec(i)
    # json.loads(json_string)
        
    return res
def format_output(x,opt=None):
    if opt:
        y = x
    else :
        y = x
    return y

def format_input(x,opt=None):
    return x

if __name__ == "__main__":
    main(sys.argv)