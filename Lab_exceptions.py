# Exceptions


## Below you have a code that raises an exception , using what you learned do the following:




def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

# - Find what type of exception is raised.
try:
    additoin(10, 20)
except Exception as ex:
    error = type(ex)
    print(error)

# - Hanlde the exception in try..except 
try:
    additoin(10,20)
# - if operation fails, handle the specific exception that is raised , and print a relevant message.
except NameError as ne:
    print('there is a NameError need to be fixed!')
# - If operation successful , print "the operation is successful"
else:
    print('the operation is successful')
