# from mylib import my_square, diff

# from mylib import * 
import mylib

print(mylib.my_square(10))
grad = mylib.diff(mylib.my_square, 10)
print('Grad: ', grad)
