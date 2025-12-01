print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
#################################
import turtle
# --- Thiết lập màn hình đồ họa ---
window = turtle.Screen()
window.bgcolor("white")
window.title("Hoa Văn Hình Tròn")
# --- Thiết lập đối tượng rùa (bút vẽ) ---
painter = turtle.Turtle()
painter.pensize(2)
painter.speed(0) # Tốc độ vẽ nhanh nhất
# painter.hideturtle() # Ẩn hình rùa (tùy chọn)
# Danh sách 3 màu cần dùng
colors = ["red", "green", "blue"]
# Góc xoay cho mỗi hình tròn
# 360 độ / 18 hình = 20 độ. Ta sẽ vẽ 18 hình tròn (6 hình x 3 màu)
angle_per_circle = 360 / 18
# --- Vòng lặp chính để vẽ hoa văn ---
# Ta sẽ lặp 18 lần để đảm bảo hoa văn đóng kín (18 * 20 = 360)
for i in range(18):
    # Chọn màu dựa trên chỉ số i để lặp lại 3 màu:
    # i%3=0 (red), i%3=1 (green), i%3=2 (blue)
    current_color = colors[i % 3]
    painter.pencolor(current_color)
    # 1. Vẽ hình tròn bán kính 80 (hoặc kích thước phù hợp)
    painter.circle(80)
    # 2. Xoay rùa để chuẩn bị vẽ hình tròn tiếp theo
    painter.left(angle_per_circle)
window.mainloop()
