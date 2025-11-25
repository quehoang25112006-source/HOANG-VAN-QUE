print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
def benefit(t, n, k):
    lai_suat_thap_phan = t / 100.0
    so_tien_nhan_duoc = n * (1 + lai_suat_thap_phan) **k

    return so_tien_nhan_duoc

def nhap_du_Lieu_hop_le(ten_bien, loai=float) :
    while True:
        try:
           gia_tri = loai(input(f"Nhập {ten_bien}: "))
           if gia_tri < 0 and ten_bien != "Lãi suất t (%/tháng)":
                print(f"Lỗi: {ten_bien} không được âm. Vui lòng nhập lại.")
                continue
           if ten_bien == "số tháng gửi k" and gia_tri != int(gia_tri):
               print (f"Lỗi: {ten_bien} phải là số nguyên. Vui lòng nhập lại.")
               continue
           return gia_tri
        except ValueError:
            print("Lỗi: Đầu vào không phải là số hợp lệ. Vui lòng thử lại.")

t_lai_suat = nhap_du_lieu_hop_le("Lãi suất t (%/tháng)")
n_von_ban_dau = nhap_du_lieu_hop_le("số vốn ban đầu n")
k_so_thang= int(nhap_du_lieu_hop_le("số tháng gửi k", loai=float))

tong_tien = benefit(t_lal_suat, n_von_ban_dau, k_so_thang)
tien_lai = tong_tien - n_von_ban_dau
                                    
print("\n" + "=" * 40)
print("KẾT QUẢ TÍNH TIỀN GỬI TIẾT KIỆM")
print(f"  Vồn ban đầu (n): {n_von_ban_dau:,.Of} VNĐ")
print(f"  Lãi suất (t): {t_lai_suat}% / tháng")
print(f"  Số tháng gửi (k): {k_so_thang} tháng")
print("-" * 40)
print(f"  Tổng số tiền nhận được sau {k_so_thang} tháng: {tong_tien:,.0f} VNĐ")
print(f" ở tiền lãi nhận được: (tien_lai?,.0f) VNĐ")
print ("=" * 40)

