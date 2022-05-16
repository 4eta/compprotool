N = int(input())

import math

def is_prime(n):
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n+1):
        if n % i == 0:
            return False
    return True

def eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime


def factorization(n):
    fact = []
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n+1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            fact.append([i, cnt])
    if n != 1:
        fact.append([n,1])
    return fact