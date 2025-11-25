print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
class py_solution:
    """Class chứa phương thức đảo ngược thứ tự các từ trong một chuỗi."""
    def reverse_words(self, s):
        """
        Tách chuỗi thành các từ, đảo ngược thứ tự của danh sách từ,
        và sau đó nối chúng lại thành một chuỗi.
        # 1. Tách chuỗi thành danh sách các từ.
        #    .split() mặc định tách theo khoảng trắng và xử lý nhiễu khoảng trắng.
        """
        words = s.split()

        """
        # 2. Đảo ngược thứ tự của danh sách từ.
        #    Sử dụng slicing [::-1] để đảo ngược hiệu quả.
        """
        reversed_words = words[::-1]

        """
        # 3. Nối các từ đã đảo ngược lại thành chuỗi, cách nhau bằng khoảng trắng.
        """
        return ' '.join(reversed_words)

# Tạo đối tượng
solution = py_solution()

# Kiểm tra ví dụ
print(solution.reverse_words('hello .py'))
