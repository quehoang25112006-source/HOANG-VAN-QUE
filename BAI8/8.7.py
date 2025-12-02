print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
import tkinter
import random
from tkinter import messagebox # Thêm thư viện messagebox để hiển thị thông báo kết thúc trò chơi

# list of possible colours.
# Danh sách này được dùng cả làm text (colours[0]) và màu (colours[1])
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

# Biến điểm số
score = 0

# Biến thời gian chơi, ban đầu 120 giây (Yêu cầu Bước 2)
timeleft = 120 

# ID của vòng lặp countdown để dừng khi cần
countdown_job = None 

# Hàm bắt đầu trò chơi.
def startGame(event):
    """Bắt đầu trò chơi khi người dùng nhấn Enter."""
    global timeleft
    global countdown_job

    # Chỉ bắt đầu countdown và trò chơi nếu đang ở trạng thái ban đầu (timeleft = 120)
    if timeleft == 120:
        # Hủy vòng lặp countdown cũ (nếu có) để tránh lặp lại
        if countdown_job:
            root.after_cancel(countdown_job)
        
        # Bắt đầu bộ đếm ngược
        countdown()
        
        # Chạy hàm chọn màu tiếp theo
        nextColour()

# Function to choose and
# display the next colour.
def nextColour():
    """Chọn và hiển thị màu tiếp theo, đồng thời kiểm tra câu trả lời của người dùng."""
    global score
    global timeleft
    
    # Lấy từ người dùng nhập
    input_text = e.get().strip()
    
    # Xóa nội dung hộp nhập liệu ngay lập tức
    e.delete(0, tkinter.END)
    
    # Nếu trò chơi đang diễn ra
    if timeleft > 0:
        # Nếu đây không phải lần gọi đầu tiên (người chơi đã nhập)
        if input_text:
            # Lấy màu *hiện tại* của chữ, đây là màu mà người dùng cần đoán
            # colours[1] là màu của chữ, colours[0] là chữ được hiển thị
            current_display_colour_text = label.cget("fg")
            
            # Xử lý tính điểm (Yêu cầu Bước 3)
            # Kiểm tra xem từ nhập có trùng với màu của chữ không (không phân biệt hoa/thường)
            if input_text.lower() == current_display_colour_text.lower():
                score += 2  # Đúng: cộng 2 điểm
            else:
                score -= 1  # Sai: trừ 1 điểm
        
        # Đảm bảo hộp nhập liệu luôn được kích hoạt
        e.focus_set()
        
        # Xáo trộn danh sách màu
        random.shuffle(colours)
        
        # Hiển thị màu mới
        # Text mới (colours[0]) và màu mới (colours[1])
        label.config(
            fg = str(colours[1]), # Màu hiển thị (cần đoán)
            text = str(colours[0]) # Text hiển thị (không được đoán)
        )
        
        # Cập nhật điểm số trên giao diện
        scoreLabel.config(text = "Score: " + str(score))
        
        # Chạy lại hàm nextColour khi Enter được nhấn
        # Điều này cho phép người chơi nhập liên tục
        root.bind('<Return>', nextColour)
        
    else:
        # Nếu hết giờ, hiển thị thông báo kết thúc
        messagebox.showinfo("Game Over", f"Hết giờ! Điểm số cuối cùng của bạn là: {score}")
        # Vô hiệu hóa việc nhập liệu
        e.config(state=tkinter.DISABLED)


# Countdown timer function
def countdown():
    """Bộ đếm ngược thời gian chơi."""
    global timeleft
    global countdown_job
    
    # Nếu trò chơi đang diễn ra
    if timeleft > 0:
        # Giảm thời gian
        timeleft -= 1
        
        # Cập nhật nhãn thời gian
        timeLabel.config(text = "Time left: " + str(timeleft))
        
        # Lập lịch gọi lại hàm sau 1 giây
        countdown_job = timeLabel.after(1000, countdown)
        
    elif timeleft == 0:
        # Khi hết giờ, gọi nextColour để xử lý kết thúc game
        nextColour()
        # Ngăn không cho người chơi nhấn Enter để bắt đầu lại game (trừ khi khởi động lại app)
        root.unbind('<Return>')


# --- Driver Code ---
# tạo cửa sổ GUI
root = tkinter.Tk()

# Đặt tiêu đề
root.title("COLORGAME")

# Đặt kích thước và vị trí (sử dụng kích thước cố định để đơn giản)
root.geometry("400x250")
root.resizable(False, False) # Ngăn không cho thay đổi kích thước

# --- Phần tử giao diện ---

# Nhãn hướng dẫn
instructions = tkinter.Label(root, 
    text = "Gõ TÊN MÀU của chữ. Đừng gõ chữ được hiển thị!",
    font = ('Helvetica', 12, 'bold'),
    padx=10, pady=10
)
instructions.pack()

# Nhãn điểm số (Ban đầu là thông báo bắt đầu game)
scoreLabel = tkinter.Label(root, 
    text = "Nhấn Enter để BẮT ĐẦU",
    font = ('Helvetica', 14)
)
scoreLabel.pack()

# Nhãn thời gian còn lại (Ban đầu là 120s)
timeLabel = tkinter.Label(root, 
    text = "Time left: " + str(timeleft), 
    font = ('Helvetica', 12)
)
timeLabel.pack()

# Nhãn hiển thị màu sắc (chữ to nhất)
label = tkinter.Label(root, font = ('Helvetica', 60, 'bold'))
label.pack(pady=10)

# Hộp nhập liệu
e = tkinter.Entry(root, font = ('Helvetica', 18), justify='center')
e.pack(padx=20, pady=10, fill='x')

# Thiết lập sự kiện:
# Lần nhấn Enter đầu tiên sẽ gọi startGame
root.bind('<Return>', startGame)

# Đặt focus vào hộp nhập liệu
e.focus_set()

# Bắt đầu vòng lặp GUI
root.mainloop()
