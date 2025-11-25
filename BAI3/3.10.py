print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
import math

def Tinh(R):
    if R <= 0:
        print (f"Lỗi: Bán kính R phải lớn hơn 0. Giá trị nhập vào là {R}.")
        return None

    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    
    return chu_vi, dien_tich

while True:
   try:
      R_input = input("Nhập bán kính R của hình tròn (số dương) : ")
      R = float(R_input)
      break
   except ValueError:
       print ("Lỗi: Đầu vào không phải là một số. Vui lòng thử lại.")
       
ket_qua = Tinh(R)

if ket_qua is not None:
   chu_vi, dien_tich = ket_qua
   print("-" * 30)
   print(f"Với bán kính R ={R}:")
   print(f" Chu vi hình tròn: P= (chu_vi:.2f) (làm tròn 2 chữ số thập phân)")
   print (f" Diện tích hình tròn: s = (dien _tich:.2f) (làm tròn 2 chữ số thập phân)")
   print("-" * 30)
