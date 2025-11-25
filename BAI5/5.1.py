print("Sinh vien: Hoang Van Que")
print("Ma so SV : 245752021610045")
print("###########################")
########*##*#####################
def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    total = 0.0
    for v in values:
        total = total + v
    return float(total) / nvals
# import module

values = (2, 4, 6, 8, 10)
print('Squares:')
for v in values:
    print(square(v))

print('Cubes:')
for v in values:
    print(cube(v))

print('Average:', average(values))

print(square(2))
print(square(3))
