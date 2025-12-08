print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
###########################
s = input("Nhập các số phân 4 chữ số, cách nhau bởi dấu phẩy: ")
list_s = s.split(',') 
ket_qua = [x for x in list_s if int(x) % 5 == 0]
print(','.join(ket_qua))
