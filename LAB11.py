from logging import exception

def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

#Hanlde the exception in try..except
try:
    additoin(10, 20)

# Find what type of exception is raised, handle it and print a relevant message.
except NameError as e:
    print("the opreation fail, ErrorType:", e.__class__)


# If operation successful , print "the operation is successful"
else:
    print ("the operation is successful")    
