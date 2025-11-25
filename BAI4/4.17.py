print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
def tinh_tong_uoc(n) :
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def tim_so_co_tong_uoc_lon_hon_chinh_no():
    try:
        n = int(input("Nhap so nguyen n: "))
    except ValueError:
        print ("Gia tri nhap khong hop le.")
        return
    
    for so in range(1, n):
        if tinh_tong_uoc(so) > so:
            print(so)
            
tim_so_co_tong_uoc_lon_hon_chinh_no()
