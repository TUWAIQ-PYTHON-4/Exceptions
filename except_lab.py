


def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)
 
try:
    additoin(10, 20) 
except NameError as ne:
    print(ne.__class__)
else:
    print('The operation is successful')
