print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x100')
# 1. Widget Label để hiển thị thông báo phím bấm
lbl_key = Label(window, text="Bấm phím bất kỳ trên cửa sổ này!", font=("Arial", 12))
lbl_key.grid(column=0, row=0, padx=10, pady=10)
# 2. Xây dựng phương thức xử lý sự kiện phím bấm
def key_pressed(event):
    """Xử lý sự kiện khi một phím trên bàn phím được bấm.
    Hàm này nhận đối tượng event chứa thông tin về sự kiện."""
    # event.char chứa ký tự của phím được bấm
    key_info = f"Bạn đã bấm phím: '{event.char}'"
    lbl_key.configure(text=key_info)
# 3. Gán sự kiện phím bấm cho cửa sổ
# "<Key>" có nghĩa là bất kỳ phím nào được bấm trên cửa sổ
# Liên kết sự kiện "<Key>" với hàm key_pressed
window.bind("<Key>", key_pressed)
# Vòng lặp chính (giữ cửa sổ mở)
window.mainloop()
