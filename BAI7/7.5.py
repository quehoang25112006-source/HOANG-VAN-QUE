print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
def append_and_display_file(file_path, text_to_append):
    """Nối văn bản vào cuối tệp, sau đó đọc và in toàn bộ nội dung."""  
    # 1. Nối (thêm) văn bản vào cuối file
    try:
        with open(file_path, 'a', encoding='utf-8') as myfile:
            myfile.write(text_to_append + '\n') # Thêm nội dung và xuống dòng
    except Exception as e:
        print(f"Lỗi khi ghi file: {e}")
        return # Dừng nếu ghi file thất bại
    # 2. Đọc và hiển thị toàn bộ nội dung file
    try:
        with open(file_path, 'r', encoding='utf-8') as myfile:
            content = myfile.read()
            print("\n--- Nội dung tệp sau khi nối ---")
            print(content)
            print("---------------------------------") 
    except FileNotFoundError:
        # Trường hợp này hiếm xảy ra sau khi vừa ghi thành công
        print(f"Lỗi: Không tìm thấy file tại đường dẫn '{file_path}'")
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")
file_duong_dan = "abc.txt"
noi_dung_them = "Đây là dòng được thêm vào sau."
# Giai đoạn 1: Tạo file và thêm nội dung (Lần chạy 1)
print("\nLần chạy 1: Khởi tạo tệp.")
append_and_display_file(file_duong_dan, "Python là ngôn ngữ lập trình.")
# Giai đoạn 2: Nối thêm nội dung mới (Lần chạy 2)
print("\nLần chạy 2: Nối thêm văn bản.")
append_and_display_file(file_duong_dan, noi_dung_them)
