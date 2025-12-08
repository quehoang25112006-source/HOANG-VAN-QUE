print("Họ và tên :HOANG VAN QUE")
print("MSSV:2457520221610045")
print("#####################")
##########################
def binary_search(list, value):
    lowerbound = 0
    upperbound = len(list) - 1

    while lowerbound <= upperbound:
        midpoint = (lowerbound + upperbound) // 2
        
        if list[midpoint] == value:
            return True # Đã tìm thấy
        elif list[midpoint] < value:
            lowerbound = midpoint + 1 # Bỏ qua nửa đầu
        else:
            upperbound = midpoint - 1 # Bỏ qua nửa sau

    return False # Không tìm thấy
list = list(map(int, input("Nhập list (các số cách nhau bởi khoảng trắng): ").split()))
list.sort()
print("List sau khi sắp xếp:", list) # In list đã sắp xếp

value = int(input("Nhập giá trị cần tìm: "))

result = binary_search(list, value)
print("Kết quả:", result)


