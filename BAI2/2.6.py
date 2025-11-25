print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
numbers = []
for i in range (2000, 3201) :
    if (i % 7 == 0) and (i % 5 != 0):
        numbers.append (str (i))
        
print (','.join (numbers) )
