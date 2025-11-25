print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
def sang_erastosthenes(gioi_han) :
    is_prime = [True] * (gioi_han + 1)
    is_prime[0] = is_prime[1] = False
    
    p = 2
    while (p * p <= gioi_han):
        if is_prime[p]:
            for i in range(p * p, gioi_han + 1, p) :
                is_prime[i] = False
        p += 1
        
    so_nguyen_to = [i for i, is_p in enumerate(is_prime) if is_p]
    return so_nguyen_to

GIOI_HAN = 1000000

ds_nguyen_to = sang_erastosthenes(GIOI_HAN - 1)

P = tuple(ds_nguyen_to)

print(f" Tuple P gom {len(P)} so nguyen to nho hon 1 trieu.")
