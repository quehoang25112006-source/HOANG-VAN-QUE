print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
def find_min_max(data_list):
    """Tìm phần tử lớn nhất và nhỏ nhất của danh sách."""
    if not data_list:
        return None, None
    
    min_val = min(data_list)
    max_val = max(data_list)
    
    return min_val, max_val

def sort_list_asc(data_list):
    """Sắp xếp danh sách theo thứ tự tăng dần."""
    return sorted(data_list)

def find_min_max_index(data_list, min_val, max_val):
    """Tìm chỉ mục (index) của phần tử nhỏ nhất và lớn nhất."""
    if not data_list or min_val is None or max_val is None:
        return None, None
        
    # Sử dụng phương thức index() để tìm vị trí
    min_index = data_list.index(min_val)
    max_index = data_list.index(max_val)
    
    return min_index, max_index
