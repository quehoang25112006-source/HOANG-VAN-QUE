print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
class Hinhchunhat(object):
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    
    def dien_tich(self):
        # Cong thuc dien tich: chieu dai * chieu rong
        return self.chieu_dai * self.chieu_rong

# Tao mot doi tuong (instance) tu lop Hinhchunhat voi chieu dai 8 va chieu rong 5
hcn = Hinhchunhat(8, 5)

# Goi phuong thuc dien_tich() tren doi tuong hcn va in ket qua
print(hcn.dien_tich())
