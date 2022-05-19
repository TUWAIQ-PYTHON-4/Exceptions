def additoin(x, y):
          x = 10
          y = 20
          raise NameError ("You use not definde varible")
          print("Addition:", x + b)

try:
    additoin(10, 20)
except NameError as n:
    print(n)
else:
    print("the operation is successful")
finally:
    print("Run in all cases on failuer or success")

#additoin(10, 20)



