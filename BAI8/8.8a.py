print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
import tkinter as tk
from tkinter import ttk 
def create_personal_info_form():
    # Khởi tạo cửa sổ (root)
    info_window = tk.Tk()
    info_window.title("Thông Tin Cá Nhân")
    info_window.geometry('350x200')
    # Danh sách các trường thông tin
    labels = ["Họ Tên:", "Ngày Tháng Năm Sinh:", "MSSV:", "Ngành Học:"]
    # Tạo các Label và Entry
    # enumerate(labels) trả về (chỉ số hàng, nội dung nhãn)
    for i, text in enumerate(labels):
        # Label (Trường tiêu đề) - Dùng ttk.Label để có giao diện theme
        lbl = ttk.Label(info_window, text=text, font=('Arial', 10))
        lbl.grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        # Entry (Ô nhập liệu trống)
        entry = ttk.Entry(info_window, width=30)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky=tk.W)
    # Vòng lặp chính
    info_window.mainloop()
if __name__ == '__main__':
    create_personal_info_form()
