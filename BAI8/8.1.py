print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
import turtle
# --- Thiết lập màn hình đồ họa ---
window = turtle.Screen()
window.bgcolor("lightblue") # Đổi màu nền thành "lightblue" để dễ nhìn hơn
# --- Thiết lập đối tượng rùa (bút vẽ) ---
painter = turtle.Turtle()
painter.color('red', 'yellow') # Đặt màu bút là đỏ, màu tô là vàng
painter.pensize(2)
# --- Hàm vẽ hình vuông ---
def drawsq(t, s):
    """
    Vẽ một hình vuông với cạnh dài s sử dụng rùa t.
    """
    t.begin_fill() # Bắt đầu tô màu
    for _ in range(4):
        t.forward(s)
        t.left(90)
    t.end_fill() # Kết thúc tô màu
# --- Thiết lập ban đầu cho rùa ---
painter.speed(0) # Tốc độ vẽ nhanh nhất (hoặc 10)
# --- Vòng lặp chính để vẽ hình ---
for i in range(18):# Giảm số lần lặp để hình vẽ được quan sát và tính toán hơn (Chú thích từ ảnh)
    painter.left(20) # Xoay 20 độ theo chiều kim đồng hồ (left là ngược chiều kim đồng hồ)
    drawsq(painter, 100) # Vẽ hình vuông cạnh 100
# Giữ cửa sổ đồ họa mở
window.mainloop()
