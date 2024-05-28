

v0 = (4.018,5)
v1 = (3.69,20)
vx = (6.1,7)

v2 = (3.69,20)
v3 = (3.468,13)
v4 = (3.452,30)

t0 = (20,2)
t1 = (5,2) 
valneva_all = [v0,v1,v2,v3,v4,vx]
tests = [t0,t1]
valneva_two_first = [v0,v1,vx,v2,v3,v4]

def moyenne(lst):
    somme_v = 0
    somme_k = 0 
    for i in lst:
        somme_v += i[0] * i[1]
        somme_k += i[1]
    
    if somme_k != 0:
        print(somme_k,somme_v)
        return somme_v/somme_k
    else :
        return "No value ?"    
    
y0 = moyenne(valneva_all)
print(y0)
y1 = moyenne(valneva_two_first)
print(y1)
"""
yt0 = moyenne(tests)
print(yt0)
"""