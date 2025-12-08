print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
def sequential_search(dlist, item):
    pos = 0
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found, pos if found else -1

# Chương trình chính
dlist = list(map(int, input("Nhập danh sách các số cách nhau bởi dấu cách: ").split()))
item = int(input("Nhập phần tử cần tìm: "))

found, pos = sequential_search(dlist, item)

if found:
    print("Tìm thấy item tại vị trí (pos)", pos)
else:
    print("Không tìm thấy item trong danh sách")

