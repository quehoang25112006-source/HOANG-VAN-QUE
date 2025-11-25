print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
S = input ("Nhap chuoi co lan so: ")
S_moi = ""

for ch in S:
    if not ch.isdigit():
        S_moi = S_moi + ch
        
print(f"Chuoi sau khi loai bo so: {S_moi}")
