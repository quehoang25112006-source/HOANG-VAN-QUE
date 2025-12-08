print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
###########################
s = input("Nhập danh sách số, cách nhau bởi dấu phẩy: ")
nums =  [int(x) for x in s.split(",")]
le = [str(x) for x in nums if x % 2 != 0]
print(",".join(le))
