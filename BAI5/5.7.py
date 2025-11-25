print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
import numpy as np
# Định nghĩa kiểu dữ liệu (dtype) cho mảng có cấu trúc
# S15: chuỗi tối đa 15 ký tự, int: số nguyên, float: số thực
data_type = [('name', 'S15'), ('class', int), ('height', float)]
# Dữ liệu chi tiết của sinh viên
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5), ('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
# Sắp xếp mảng theo trường 'height'
print("\nSort by height:")
# np.sort() trả về một mảng mới đã được sắp xếp
sorted_students = np.sort(students, order='height')
print(sorted_students)
