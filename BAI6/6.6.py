print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
# Thông tin sinh viên
print("Sinh viên: Cao Xuan Thang")
print("Ma so SV : 245752021610145")
print("#####################################")

class IOString(object):
    """Class chứa phương thức nhận chuỗi và in in hoa."""
    def __init__(self):
        """Khởi tạo thuộc tính str1."""
        self.str1 = ""
    def get_String(self):
        """Chấp nhận chuỗi từ người dùng."""
        self.str1 = input("Vui lòng nhập một chuỗi: ")
    def print_String(self):
        """In chuỗi đã nhập bằng chữ in hoa."""
        print(self.str1.upper())
# Tạo đối tượng
str1 = IOString()
# Sử dụng các phương thức
str1.get_String()
str1.print_String()
