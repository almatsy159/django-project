#import cv2 as cv
import os
import re
import sys 

lst_img_format = ["jpeg","png","gif","pdf","ai","svg"]
cpt = 0
lst_exp = []

while cpt < len(lst_img_format) and cpt<100:
    my_str = f'format{cpt} = r".\.{lst_img_format[cpt]}"' 
    lst_exp.append(my_str)
    cpt += 1
    
def get_img_from_dir(dir="",exp=None):
    print(exp)
    if dir == "":
        dir = "/"
        print(os.getcwd())
    lst_img = []
    for fname in os.listdir(dir):
        x = re.search(exp,fname)
        if x:
            lst_img.append(fname)
    #print(lst_img)
    return lst_img
        

        
path = input("enter path toward images")
images = []
for e in lst_exp:
    res = get_img_from_dir(path,e)
    for i in res:
        images.append(i)
        
print(images)
    

#### opencv start here #####

#img0 = cv.imread("/Documents/Image/") 