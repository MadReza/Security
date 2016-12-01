import random
import math

def Miller(value, iteration):
    """Determins if the value is prime probably"""
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
        mod = math.pow(a, temp) % value

        while temp != value-1 and mod != 1 and mod != value-1:
            mod = (mod*mod) % value
            temp *= 2

        if mod != value-1 and temp%2 == 0:
            return False

        iteration = iteration -1
    return True


for x in range(3, 50):
    print x, Miller(x, 5)

