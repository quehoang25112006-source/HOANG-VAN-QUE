print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
def count_lines(file_path):
    """Đếm và in ra tổng số dòng trong tệp."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # Phương pháp hiệu quả: đọc tất cả các dòng vào list
            line_count = len(f.readlines()) 
            print(f"Tổng số dòng trong tệp là: {line_count}")         
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
count_lines('C:/QUE/a.txt')
