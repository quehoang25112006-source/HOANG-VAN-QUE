print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# 1. Sử dụng np.lexsort() để lấy chỉ số sắp xếp
# Chú ý: lexsort sắp xếp dựa trên các cột theo thứ tự từ PHẢI sang TRÁI.
# Ta muốn sắp xếp theo chiều cao (cấp 1) rồi mới đến ID (cấp 2).
# Thứ tự truyền vào: (cột cấp 2, cột cấp 1)
# Sắp xếp theo: student_height (chính) và student_id (phụ)
indices = np.lexsort((student_id, student_height))

print("Chỉ số:")
print(indices)

print("\nDữ liệu sắp xếp:")

# 2. Áp dụng chỉ số sắp xếp lên cả hai mảng
# Mảng ID được sắp xếp theo chiều cao, sau đó là ID (cho các trường hợp chiều cao bằng nhau)
sorted_id = student_id[indices]
sorted_height = student_height[indices]

# In dữ liệu đã sắp xếp theo định dạng yêu cầu
for i in range(len(sorted_id)):
    # Sử dụng f-string để căn lề cho đẹp
    print(f"{sorted_id[i]:<7} {sorted_height[i]:>5.1f}")
