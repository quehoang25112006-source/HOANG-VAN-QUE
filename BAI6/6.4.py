print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
##################################
class py_solution(object):
    """
    Class chua phuong thuc chuyen doi so La Ma sang so nguyen.
    """
    def roman_to_int(self, s):
        """
        Chuyen doi chuoi so La Ma (s) thanh so nguyen.
        Su dung quy tac cong (I, V, X, L, C, D, M) va quy tac tru
        """
        # Dinh nghia gia tri cho tung ky tu La Ma
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        # Duyet qua chuoi so La Ma
        for i in range(len(s)):
            # Quy tac trừ: Nếu ký tự hiện tại có giá trị nhỏ hơn ký tự tiếp theo, 
            # thì trừ giá trị của ký tự hiện tại.
            # Ta chi can kiem tra neu i + 1 < len(s) va gia tri hien tai < gia tri ke tiep.
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                # Cong thuc: int_val = int_val + rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                # Vi du: IV (int_val dang la 1) -> 1 + 5 - 2*1 = 4
                # Day la cach tinh toan de bu tru cho lan cong truoc do
                int_val = int_val + rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                # Quy tac cộng: Cộng giá trị của ký tự hiện tại.
                int_val += rom_val[s[i]]
        return int_val
# Tao doi tuong
solution = py_solution()
# Kiem tra vi du
print(solution.roman_to_int('MMMCMXCVII')) 
print(solution.roman_to_int('MCMXCIV')) 
print(solution.roman_to_int('C'))         
