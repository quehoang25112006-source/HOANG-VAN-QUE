print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
def write_list_to_file(file_path, data_list):
    """Ghi nội dung của danh sách vào tệp, mỗi phần tử một dòng."""
    try:
        # Mở file ở chế độ ghi ('w') để ghi đè hoặc tạo mới
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in data_list:
                f.write(item + '\n') 
        print(f"Đã ghi {len(data_list)} mục từ danh sách vào tệp: {file_path}")
        # Đọc lại và hiển thị để xác nhận
        with open(file_path, 'r', encoding='utf-') as f:
            print("\nNỘI DUNG ĐÃ GHI:")
            print(f.read())
    except Exception as e:
        print(f"Đã xảy ra lỗi khi ghi file: {e}")
shopping_list = ["Mía", "Sữa tươi", "Bánh mì", "Rau Củ"]
write_list_to_file('C:/QUE/shopping_list.txt', shopping_list)
