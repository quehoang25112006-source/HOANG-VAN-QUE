print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
###########################
s = input("Nhập câu: ")
chu_hoa = sum([c.isupper() for c in s])
chu_thuong = sum([c.islower() for c in s])
print("Chữ hoa:", chu_hoa)
print("chữ thường:", chu_thuong)
