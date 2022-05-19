


def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)



try:
    additoin(x, y)
except NameError as e:
    print(e.__class__,"Raised when a variable is not found in the local or global scope.")
else:
    print("the operation is successful")
        
