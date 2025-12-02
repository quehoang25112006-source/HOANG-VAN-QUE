print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
def cut_list(input_list):
    """
    Trả về một list mới bằng cách bỏ đi phần tử đầu tiên 
    và phần tử cuối cùng của list gốc.
    
    Tham số:
    input_list (list): List đầu vào.
    
    Trả về:
    list: List đã cắt.
    """
    # [1:-1] có nghĩa là: 
    # - Bắt đầu từ index 1 (phần tử thứ hai, bỏ phần tử đầu tiên có index 0).
    # - Kết thúc ở index -1 (trước phần tử cuối cùng).
    
    # Kiểm tra list có ít nhất 2 phần tử không (để cắt được cả đầu và cuối)
    if len(input_list) >= 2:
        return input_list[1:-1]
    else:
        # Trả về list rỗng nếu list quá ngắn
        return []

# --- Ví dụ minh họa ---
list_a = [10, 20, 30, 40, 50, 60]
list_b = ["apple", "banana", "cherry", "date"]
list_c = [1, 2]
list_d = [5]

result_a = cut_list(list_a)
result_b = cut_list(list_b)
result_c = cut_list(list_c)
result_d = cut_list(list_d)


print(f"List gốc A: {list_a}")
print(f"List đã cắt A (bỏ 10 và 60): {result_a}")
print("-" * 20)

print(f"List gốc B: {list_b}")
print(f"List đã cắt B (bỏ 'apple' và 'date'): {result_b}")
print("-" * 20)

print(f"List gốc C: {list_c}")
print(f"List đã cắt C (chỉ còn 2 phần tử, trả về rỗng): {result_c}")
print("-" * 20)

print(f"List gốc D: {list_d}")
print(f"List đã cắt D (chỉ còn 1 phần tử, trả về rỗng): {result_d}")
