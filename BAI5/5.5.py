print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
def find_min_max(data_list):
    """Tìm phần tử lớn nhất và nhỏ nhất của danh sách."""
    if not data_list:
        return None, None
    
    # Python built-in functions
    min_val = min(data_list)
    max_val = max(data_list)
    
    return min_val, max_val

def sort_list_asc(data_list):
    """Sắp xếp danh sách theo thứ tự tăng dần."""
    # Trả về một bản sao đã được sắp xếp
    return sorted(data_list)
