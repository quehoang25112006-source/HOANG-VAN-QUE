print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
###########################
def bubbleSort(nlist):
    loop = len(nlist)
    for i in range(loop-1):
        swapped = False
        for j in range(loop-i-1):
            # So sánh các phần tử cạnh nhau
            if nlist[j] > nlist[j+1]:
                # Trao đổi chúng
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        # Nếu không có trao đổi nào, list đã được sắp xếp, thoát khỏi vòng lặp
        if not swapped:
            break
    return nlist

# Chương trình chính
n = int(input("Nhập số lượng phần tử: "))
nlist = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(element)

# Sắp xếp danh sách
sorted_list = bubbleSort(nlist)

# In kết quả
print("Danh sách đã sắp xếp:", sorted_list)
