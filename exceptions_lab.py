# Find what type of exception is raised of this function
def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)




# Handle the exception in try..except
try:
    additoin(10, 20)
except NameError:
        print("Variable within the function is not valid causing Name Error")
else:
        print("The operation is successful")

