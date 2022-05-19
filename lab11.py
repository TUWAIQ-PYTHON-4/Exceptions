def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
try:
    additoin(10, 20)
except NameError:
    print("Name not defined globally")
except Exception as e: # here we define the specefic erorr
    print(e.__class__,NameError.__doc__)
else:
    print("the operation is successful")