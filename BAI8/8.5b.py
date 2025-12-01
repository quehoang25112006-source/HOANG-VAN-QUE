print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
import tkinter as tk
# 1. Xây dựng cửa sổ gốc (root)
root = tk.Tk()
root.title("tk") # Đặt tiêu đề đơn giản như trong hình
# 2. Tạo biến kiểm soát (Control Variable)
v = tk.IntVar()
v.set(1) # Giá trị mặc định là 1 (Python 1)
# 3. Định nghĩa danh sách các lựa chọn (text và value)
languages = [
    ("Python 1", 1), # Đã thay đổi text để giống hình
    ("Perl 2", 2),
    ("Java 3", 3),
    ("C++ 4", 4),
    ("C 5", 5)
]
# 4. Phương thức xử lý sự kiện
def ShowChoice():
    """In ra giá trị (value) của Indicator Button hiện đang được chọn."""
    print(f"Giá trị đã chọn: {v.get()}")
# 5. Thêm Label tiêu đề
tk.Label(
    root,
    text="Choose your favourite programming language:",
    justify=tk.LEFT,
    padx=20,
    bg="lightgray" # Đặt màu nền cho Label để giống hình
).pack(fill=tk.X) # Dùng fill=tk.X để Label kéo dài hết chiều ngang
# 6. Tạo và đóng gói các Indicator Button
for text, val in languages:
    tk.Radiobutton(
        root,
        text=text,
        padx=20,
        variable=v,
        command=ShowChoice,
        value=val,
        indicatoron=0, # Tắt nút tròn (radio button) truyền thống
        width=20, # Đặt chiều rộng cố định cho nút (được tính bằng số ký tự)
        anchor=tk.W, # Căn lề nội dung trong nút
        bd=1, # Đường viền mỏng (Border width)
        relief=tk.RIDGE # Kiểu đường viền để tạo cảm giác phân cách giữa các nút
    ).pack(fill=tk.X) # Dùng fill=tk.X để nút kéo dài hết chiều ngang
# 7. Vòng lặp chính để hiển thị cửa sổ
root.mainloop()
