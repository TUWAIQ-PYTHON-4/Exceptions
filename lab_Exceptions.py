'''
# Exceptions


## Below you have a code that raises an exception , using what you learned do the following:
- Find what type of exception is raised.
- Hanlde the exception in try..except 
- If operation successful , print "the operation is successful"
- if operation fails, handle the specific exception that is raised , and print a relevant message.

      def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)


      additoin(10, 20)

'''

'''

def additoin(x, y):
        try:
           x = 10
           y = 20
           print("Addition:" , x + y)
        except operation_fails as a:
            print(a)
        else:
            print("the operation is successful")
        
'''

from decimal import DivisionByZero


def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
   additoin(10, 0)
except NameError as ne:
    print("the opration is fail becouse you have name error")
except Exception as er:
    print(er.__class__)
else:
    print("the operation is successful")

 