print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
def count_file_stats(file_path):
    """Đọc file và tính số ký tự, số từ, và số dòng."""  
    char_count = 0  
    word_count = 0  
    line_count = 0     
    try:
        # Mở tệp ở chế độ 'r' (read)
        with open(file_path, 'r') as f:
            for line in f:
                line_count += 1
                char_count += len(line)
                # Loại bỏ khoảng trắng thừa và ký tự xuống dòng ở hai đầu
                words = line.strip().split() 
                word_count += len(words) 
        # In kết quả
        print(f"Số ký tự (bao gồm khoảng trắng và ký tự xuống dòng) là: {char_count}")
        print(f"Số từ là: {word_count}")
        print(f"Số dòng là: {line_count}")          
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_duong_dan = 'C:/QUE/a.txt'
count_file_stats(file_duong_dan)
