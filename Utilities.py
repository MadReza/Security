import random
import math

def mulmod(a, b, c):
    """calculates (a*b)%c. Solved Math Overflow errors"""
    x = 0
    y = a % c
    
    while b > 0:
        if b % 2 == 1:
            x = (x+y) % c
        y = (y*2) % c
        b = b / 2
    return x % c

def modulo(a, b, c):
    """Calculates a^b % c. Solved for Math overflow errors"""
    res = 1
    i = 0

    while i < b:
        res = res * a
        res = res % c
        i = i + 1
    return res % c

def Miller(value, iteration):
    """Determins if the value is prime probably using the Rabin-Miller test"""
    """https://www.topcoder.com/community/data-science/data-science-tutorials/primality-testing-non-deterministic-algorithms/"""
    if value < 2:
        return False

    if value != 2 and value % 2 == 0:
        return False

    s = value - 1

    while s % 2 == 0:
        s = s / 2

    while iteration:
        a = random.randint(1, value-1)
        temp = s
        mod = modulo(a, temp, value)

        while temp != value-1 and mod != 1 and mod != value-1:
            mod = mulmod(mod, mod, value)
            temp *= 2

        if mod != value-1 and temp%2 == 0:
            return False

        iteration = iteration -1
    return True

def generate_prime(k):
    """generate a number of k bits"""
    x = k
    x = x + random.randint(1, 1000)

    while Miller(x, 5) == False:
        #x = x + 1
        x = x + random.randint(1, 1000)
    return x


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    """http://stackoverflow.com/a/9758173/205110"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
