from logging import exception


def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


try :
    additoin(10, 20)
except NameError as n :
    print(n.__class__ , "variable is not defined." )
else :
    print("the operation is successful")


