class ValueError(Exception):

 def addition(x, y):
    x = 10
    y = 20
    print("Addition:", x + y)
    raise ValueError("please enter a int value!")


 try:
    addition('e','r')
 except ValueError as ve:
    print(ve.__class__)
 finally:
    print("the operation is successful")





