import math

# returneaza True daca x este prim, False in caz contrar
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

n = int(input("Dati n: "))

# returneaza valoarea celuil de al n-lea termen din sirul dat
def n_term(n):
    if n == 1:
        return 1
    index = 1
    num = 2
    while index < n:
        if is_prime(num):
            index += 1
            if index == n:
                return num
        else:
            temp = num
            d = 2
            while temp > 1:
                if temp % d == 0:
                    for i in range(d):
                        index += 1
                        if index == n:
                            return d
                while temp % d == 0:
                    temp //= d
                if d == 2:
                    d = 3
                else:
                    d += 2
        num += 1
        
"""
t = n_term(n)
print(f"Al n-lea termen din sir este: {t}")

"""
for i in range(1, n):
    t = n_term(i)
    print(f"Al {i}-lea termen din sir este: {t}")
