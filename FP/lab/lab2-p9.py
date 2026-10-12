def palindrom1(x):
    return int(x[::-1])


def palindrom2(x):
    p = 0
    x = int(x)
    while x != 0:
        p = p * 10 + x % 10
        x //= 10
    return p


x = input("Dati numarul: ")
n = palindrom2(x)
print(f"Palindromul lui {x} este: {n}")

