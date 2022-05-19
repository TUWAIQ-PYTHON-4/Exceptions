


def additoin(x, y):
     x = 10
     y = 20
     print("Addition:", x + b)

try:
  additoin(10, 20)

except NameError as err:
    print(err)
else:
    print('the operation is successful')




def positive_num(num):
    if num < 0 :
        raise Exception('The number is not positive')
    
    print('the operation is fails')

try:
    positive_num(-1)
except Exception as e:
    print(e)
else :
    print('the operation is successful')







