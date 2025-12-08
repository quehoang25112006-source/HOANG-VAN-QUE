print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
###########################
ket_qua = []
for i in range(2000, 3201):
    if (int(i) % 4 == 0) and (int(i) % 7 != 0):
        ket_qua.append(str(i))
print(','.join(ket_qua))
