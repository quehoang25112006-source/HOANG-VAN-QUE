print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    # Dinh nghia lai (override) phuong thuc getGender() tu lop cha
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    # Dinh nghia lai (override) phuong thuc getGender() tu lop cha
    def getGender(self):
        return "Nữ"

# Tao doi tuong
aNam = Nam()
aNu = Nu()

# Goi phuong thuc getGender() tren tung doi tuong
# Moi doi tuong tra ve ket qua khac nhau (Da hinh)
print(aNam.getGender())
print(aNu.getGender())
