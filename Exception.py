



from logging import exception
from unicodedata import name


def additoin(x, y):
   
    x = 10
    y = 20   
    print("Addition:", x +b)
        


try:
    additoin(10, 20)
except  Exception as name_ER:
    print("Name Error\n",name_ER.__class__)        
else:
    print("the operation is successful")
