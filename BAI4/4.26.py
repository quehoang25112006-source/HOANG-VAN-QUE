print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
###########################
tong = 0
while True:
    s = input("Nhập giao dịch (D/W số tiền), hoặc Enter để dừng: ") 
    if not s: 
        break
    loai, so = s.split()
    so = int(so)
    loai = loai.upper()
    if loai == "D":
        tong += so
    elif loai == "W":
        tong -= so
        
print("Số tiền thực của tài khoản là:", tong)
