print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
###########################
s = input("Nhập câu: ")
chu_cai = sum([c.isalpha() for c in s])
chu_so = sum([c.isdigit() for c in s])
print("số chữ cái là:", chu_cai)
print("số chữ số là:", chu_so)
