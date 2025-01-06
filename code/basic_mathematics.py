# val = int(input())

val_List = list(map(int, input().split(" ")))


# limits = list(map(int, input().split(" ")))


# 1.Program to print the given number is even or not
def evenCheck(n):
    if n % 2 == 0:
        return True
    else:
        return False


# 2.Prime or not
def primeCheck(n):
    prime = True
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            prime = False
    return prime


# 3.print all prime numbers between range
def range_prime(a, b):
    res = []
    for i in range(a, b + 1):
        if primeCheck(i):
            res.append(i)
    return res


# 4.Pronic number or not
def pronic_number(n):
    pronic = False
    if pronic == 0: pronic = True
    for i in range(1, (n // 2) + 1):
        if i * (i + 1) == n:
            pronic = True
    return pronic


# 5.perfect number or not
def perfect_number(n):
    sum_fact = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            print(i)
            sum_fact += i
    if sum_fact == n:
        return True
    else:
        print(sum_fact)
        return False


# 6.gcd and lcm
def lcm_gcd(a, b):
    a2 = a
    b2 = b
    while b:
        a, b = b, a % b
    gcd = a
    lcm = (a2 * b2) // gcd

    return lcm, gcd

# 7.factorial without recursion

