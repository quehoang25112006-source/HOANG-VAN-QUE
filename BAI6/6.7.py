print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
###################################
import math 
class Circle(object):
    """Class đại diện cho hình tròn và tính toán các thuộc tính của nó."""
    def __init__(self, radius):
        """Phương thức khởi tạo: Thiết lập bán kính."""
        self.radius = radius
    def area(self):
        """Tính diện tích hình tròn (PI * r^2)."""
        # Công thức: S = PI * r^2
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        """Tính chu vi hình tròn (2 * PI * r)."""
        # Công thức: C = 2 * PI * r
        return 2 * math.pi * self.radius
# Tạo đối tượng
my_circle = Circle(5) # Bán kính r = 5
# In kết quả
print('\n--- Kết quả Hình tròn ---')
print(f'Bán kính: {my_circle.radius}')
print(f'Diện tích: {my_circle.area()}')
print(f'Chu vi: {my_circle.perimeter()}')
