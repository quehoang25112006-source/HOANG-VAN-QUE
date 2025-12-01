print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
from tkinter import *
def clicked():
    lbl.configure(text="Màu của Button đã được thay đổi!")
window = Tk()
window.title("Thay Đổi Màu Button")
window.geometry('350x150')
lbl = Label(window, text="Nhấn nút để kiểm tra màu sắc")
lbl.grid(column=0, row=0, padx=10, pady=10)
# Thay đổi màu nền (bg) và màu chữ (fg) của button
btn = Button(
    window,
    text="Click Me",
    command=clicked,
    # Đặt màu nền (Background) là xanh lá
    bg="green",
    # Đặt màu chữ (Foreground) là trắng
    fg="white",
    # Đặt phông chữ Arial, cỡ 10, kiểu đậm
    font=("Arial", 10, "bold")
)
btn.grid(column=0, row=1, padx=10, pady=5)
window.mainloop()
