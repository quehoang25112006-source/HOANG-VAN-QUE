print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
import re

passwords = input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ").split (',')

valid_passwords = []

for p in passwords:
    p = p.strip()
    
    if len(p) < 6 or len(p) > 12:
        continue
    
    if not re.search("[a-z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p) :
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    
    valid_passwords.append (p)
    
print ("Mật khẩu hợp lệ:", ",".join(valid_passwords))
