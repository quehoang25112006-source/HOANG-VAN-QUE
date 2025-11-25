print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
def tam_giac_pascal(n):
    if n <= 0:
        return
    dong_truoc = [1]
    print(dong_truoc)
    for i in range(1, n):
        dong_hien_tai = [1]
        for j in range(1, len(dong_truoc)):
            gia_tri = dong_truoc[j-1] + dong_truoc
            dong_hien_tai.append(gia_tri)
        dong_hien_tai.append(1)
        print(dong_hien_tai)
        dong_truoc = dong_hien_tai
try:
    n = int(input("Nhap so dong n: "))
    tam_giac_pascal(n)
except ValueError:
    print("Gia tri nhap khong hop le.")
