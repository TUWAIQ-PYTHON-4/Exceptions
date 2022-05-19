def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)



try:
  additoin(10, 20)
except Exception as e:
    print(f'an error occured of type {e.__class__}')
else:
    print("the operation is successful")
