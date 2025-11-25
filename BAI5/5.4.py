print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
import numpy as np

# Tạo một mảng (array) chứa các số nguyên từ 12 đến 37
x = np.arange(12, 38)

# Đảo ngược mảng bằng cách sử dụng kỹ thuật slicing
# [::-1] có nghĩa là: [start:stop:step], với step = -1 sẽ đảo ngược thứ tự
x_reversed = x[::-1]

print('Mảng được tạo:')
print(x)
print('\nMảng đảo ngược:')
print(x_reversed)
