print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
def binary_search(dlist, value):
    """
    Thực hiện tìm kiếm nhị phân (Binary Search) trong danh sách đã sắp xếp.
    Trả về True và vị trí (index) nếu tìm thấy, ngược lại trả về False và -1.
    """
    first = 0
    last = len(dlist) - 1
    found = False
    
    # Vị trí ban đầu là -1 (chưa tìm thấy)
    position = -1

    while first <= last and not found:
        # Tính chỉ mục giữa
        midpoint = (first + last) // 2
        
        if dlist[midpoint] == value:
            found = True
            position = midpoint
        elif value < dlist[midpoint]:
            # Nếu giá trị cần tìm nhỏ hơn, tìm ở nửa đầu
            last = midpoint - 1
        else:
            # Nếu giá trị cần tìm lớn hơn, tìm ở nửa sau
            first = midpoint + 1

    # Trả về kết quả tìm kiếm và vị trí
    if found:
        return True, position
    else:
        return False, -1
