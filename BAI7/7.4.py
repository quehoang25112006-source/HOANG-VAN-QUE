print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
def read_first_n_lines(file_path, n):
    """Đọc và in ra n dòng đầu tiên của tệp."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    # Dừng nếu hết file trước khi đạt đến n dòng
                    break
                print(line, end='') 
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'C:/QUE/B.txt'
so_dong = 3
read_first_n_lines(file_duong_dan, so_dong)
