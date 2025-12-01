print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
from tkinter import *
# Hàm xử lý khi nút bấm được click
def clicked():
    # Cập nhật thuộc tính 'text' của Label (lbl)
    lbl.configure(text="Button was clicked !!")
# --- Khởi tạo và Cấu hình Cửa sổ Chính ---
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
# --- 1. Thêm Label (Nhãn) ---
# Khởi tạo Label với văn bản mặc định là "Hello"
# Đặt Label trong cửa sổ 'window'
lbl = Label(window, text="Hello")
# Sử dụng grid layout: đặt Label ở cột 0, hàng 0
lbl.grid(column=0, row=0)
# --- 2. Thêm Button (Nút bấm) và liên kết với hàm 'clicked' ---
btn = Button(window, text="Click Me", command=clicked)
# Sử dụng grid layout: đặt Button ở cột 1, hàng 0
# Đặt nút ở cột 1, hàng 0
btn.grid(column=1, row=0)
# Vòng lặp chính (giữ cửa sổ mở)
window.mainloop()
