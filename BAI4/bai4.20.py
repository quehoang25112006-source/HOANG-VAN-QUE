print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
import math

def generate_fibonacci_tuple(N):
    """
    Tạo tuple chứa các số Fibonacci nhỏ hơn hoặc bằng N.
    """
    # Xử lý N âm
    if N < 0:
        return ()
    
    # Dãy Fibonacci bắt đầu với 0 và 1
    a, b = 0, 1
    fib_list = []
    
    while a <= N:
        fib_list.append(a)
        # Cập nhật số tiếp theo
        a, b = b, a + b
    
    # Chuyển list thành tuple và trả về
    return tuple(fib_list)

# --- Ví dụ theo yêu cầu ---
N = 100
fib_tuple = generate_fibonacci_tuple(N)

print(f"--- Kết quả Bài 20 ---")
print(f"Số N nhập vào: {N}")
print(f"Tuple các số Fibonacci nhỏ hơn hoặc bằng {N}: {fib_tuple}")

# Ví dụ với N = 10
N_example = 10
fib_tuple_example = generate_fibonacci_tuple(N_example)
print(f"Tuple các số Fibonacci nhỏ hơn hoặc bằng {N_example}: {fib_tuple_example}")
