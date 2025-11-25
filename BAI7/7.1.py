print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
def reverse_file_contents(file_path):
    """Đọc file và in nội dung của từng dòng theo thứ tự đảo ngược."""
    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            # Lặp qua từng dòng trong tệp
            for line in input_file:
                # 1. Xử lý dòng để đảo ngược
                reversed_line = line.rstrip('\n')[::-1] 
                print(reversed_line)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'C:/QUE/a.txt'
reverse_file_contents(file_duong_dan)
