import colorama

#print(colorama.Fore.RED+"hello")


def generateN3plusK(n=1,k=0,max=200):
    #res = {}
    res =[]
    for i in range(max):
        #res[i] = n*i+ k
        res.append(n*i+k)
        
    return res

maxi = 50
N3p0 = generateN3plusK(3,0,maxi)
N3p1 = generateN3plusK(3,1,maxi)
N3p2 = generateN3plusK(3,2,maxi)
#print(N3p1)


def tri_pair_impair(lst,test_value=1):
    res = []
    js_lst = []
    name = ""
    if test_value == 1:
        name = "impair"
    else :
        name = "pair"
        test_value = 0
    for i in lst:
        #print(i,i%2)
        if i%2 == test_value :
            res.append(i)
        #else : 
        #    res.append("none")
    js_lst = {name:lst}
    
    return res

print("2mod3 et impair : ",tri_pair_impair(N3p2))
print("1mod3 et pair : ",tri_pair_impair(N3p1,0))

def num_as_sum(val,base=10):
    sres = ""
    l = len(val)
    for i in range(l):
        tmp = f"{val[i]} * {base}**{l-1-i}"
        if i != l-1:
            tmp += " + "
        sres += tmp
        print(tmp)
    return sres

"""
def count_base(l=8,base=2):
    res = {}
    #nombre de charactere
    for k in range(len):
        for i in range(base):
            res[k*i+i]= 
"""            
            
my_test ="100001"
base_test = 2
x = (num_as_sum(my_test,base_test))
print(f"{eval(x)} = {x} = {my_test}({base_test})")


class Number :
    def __init__(self,val,base):
        self.val = val
        self.base = base
        self.sval = f"{self.val}"
        self.l = len(self.sval)
        
    def __str__(self):
        return f"{self.val}"
    
    def __equal_sum__(self):
        pass
        
