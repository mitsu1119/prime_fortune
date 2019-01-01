import sys
import random
import math

def MR(n):
    if n == 2:
        return True
    if n == 1:
        return False
    if n & 1 == 0:
        return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d //= 2

    for i in range(100):
        a = random.randint(1, n - 1)
        x = pow(a, d, n)
        t = d

        while t != n - 1 and x != 1 and x != n - 1:
            x = pow(x, 2, n)
            t *= 2

        if x != n - 1 and x & 1 == 0:
            return False

    return True

def isPrime(num):
    if MR(num) == True:
        print("Prime!!!")
    else:
        print("not Prime orz")

def genPrime(digit):
    while True:
        rand = random.randint(pow(10, digit - 1), pow(10, digit) - 1)
        if MR(rand) == True:
            print("あなたの運勢は {} です。".format(rand))
            return

if __name__ == "__main__":
    if sys.argv[1] == "--generate":
        genPrime(int(sys.argv[2]))
    elif sys.argv[1] == "--decision":
        isPrime(int(sys.argv[2]))
    else:
        print("command error")
