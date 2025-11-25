print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
def Sequential_Search(dlist, item):
    """
    Thực hiện tìm kiếm tuần tự (Sequential Search) trong danh sách dlist.
    Trả về True và vị trí (index) nếu tìm thấy, ngược lại trả về False và -1.
    """
    pos = 0
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1

    # Trả về kết quả tìm kiếm và vị trí
    if found:
        return True, pos
    else:
        return False, -1
