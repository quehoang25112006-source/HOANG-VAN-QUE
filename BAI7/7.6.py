print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
def read_last_n_lines(file_path, n):
    """Đọc và in ra n dòng cuối cùng của tệp."""
    try:
        # Mở tệp ở chế độ 'r' (read)
        with open(file_path, 'r', encoding='utf-8') as f:
            # 1. Đọc tất cả các dòng vào một danh sách
            all_lines = f.readlines()
            # 2. Lấy n dòng cuối cùng
            # Nếu n lớn hơn số dòng thực tế, nó sẽ lấy toàn bộ
            last_n_lines = all_lines[-n:]          
            # 3. In các dòng cuối cùng ra màn hình
            for line in last_n_lines:
                # end='' đảm bảo print không tự thêm ký tự xuống dòng
                print(line, end='') 
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'C:/QUE/b.txt'
so_dong = 3
read_last_n_lines(file_duong_dan, so_dong)
