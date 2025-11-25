print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        # Cong thuc dien tich hinh tron: Pi * r^2. Su dung 3.14 lam gia tri Pi.
        return self.radius**2 * 3.14
# Tao mot doi tuong (instance) tu lop Circle voi ban kinh r = 2
aCircle = Circle(2)
# Goi phuong thuc area() tren doi tuong aCircle va in ket qua
print(aCircle.area())
