
def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0: 
            return False  
    return True

n = int(input(">> nhap so tu nhien: "))

if is_prime(n):
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai so nguyen to")
