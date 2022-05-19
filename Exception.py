



from logging import exception
from unicodedata import name


def additoin(x, y):
    if NameError == True:
        raise NameError("Name Error")  
    x = 10
    y = 20   
    print("Addition:", x +b)
        


try:
    additoin(10, 20)
except  NameError:
    print("Name Error")        
except Exception as name_ex:
    print(name_ex,name_ex.__class__)   
finally:
    print("the operation is successful")