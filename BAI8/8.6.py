print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
from tkinter import *
from tkinter import messagebox 
# --- Định nghĩa các phương thức xử lý sự kiện ---
def OpenFile():
    """Thực hiện chức năng Mở/Tạo File mới."""
    messagebox.showinfo("Chức năng File", "Thực hiện chức năng Mở/Tạo File mới!")
def Exit():
    """Xử lý sự kiện thoát khỏi ứng dụng."""
    if messagebox.askyesno("Thoát", "Bạn có chắc chắn muốn thoát ứng dụng không?"):
        root.quit() # Thoát khỏi vòng lặp chính và đóng ứng dụng
def InsText():
    """Thực hiện chức năng Chèn Văn bản."""
    messagebox.showinfo("Chèn", "Thực hiện chức năng Chèn Văn bản.")
def InsPic():
    """Thực hiện chức năng Chèn Hình ảnh."""
    messagebox.showinfo("Chèn", "Thực hiện chức năng Chèn Hình ảnh.")
def About():
    """Hiển thị thông tin về ứng dụng."""
    messagebox.showinfo("Về Ứng Dụng", "Đây là ứng dụng Tkinter Menu Demo.")
# --- Xây dựng cấu trúc Menu và Cửa sổ Chính ---
root = Tk()
root.title("tk") # Đặt tiêu đề là "tk"
root.geometry('300x150') # Đặt kích thước để dễ nhìn
# 1. Tạo Menu Bar chính
menu = Menu(root)
root.config(menu=menu) # Gán Menu Bar vào cửa sổ gốc (root)
# 2. Tạo Menu File
filemenu = Menu(menu, tearoff=0) # tearoff=0 loại bỏ đường kẻ gạch ngang ở đầu menu
menu.add_cascade(label="File", menu=filemenu) # Thêm File menu vào Menu Bar
filemenu.add_command(label="New", command=OpenFile) # Thêm mục "New"
filemenu.add_command(label="Open", command=OpenFile) # Thêm mục "Open"
filemenu.add_separator() # Thêm đường phân cách
filemenu.add_command(label="Exit", command=Exit) # Thêm mục "Exit"
# 3. Tạo Menu Insert
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu) # Thêm Insert menu vào Menu Bar
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)
# 4. Tạo Menu Help
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu) # Thêm Help menu vào Menu Bar
helpmenu.add_command(label="About...", command=About)
root.mainloop()
