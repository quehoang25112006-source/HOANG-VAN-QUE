print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
ds = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# 1. Sắp xếp list tại chỗ (thay đổi ds gốc)
print("--- Kết quả Sắp xếp dùng .sort() ---")
ds.sort()
print(f"List sau khi sắp xếp (dùng .sort()): {ds}")


# 2. Sắp xếp list bằng hàm sorted() (tạo list mới)
new_list = ['grape', 'fig', 'kiwi', 'lemon']
print("\n--- Kết quả Sắp xếp dùng sorted() ---")
sorted_new_list = sorted(new_list)
print(f"List gốc: {new_list}")
print(f"List đã sắp xếp (dùng sorted()): {sorted_new_list}")
