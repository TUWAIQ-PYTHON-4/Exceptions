def additoin(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)


additoin(10, 20)

try:
    additoin(10, 20)
except NameError as e:
    print("the operation is not allowed")
else:
    print("the operation is successful")
