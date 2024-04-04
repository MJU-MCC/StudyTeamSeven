import math

def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n, k = map(int, input().split())
print(combination(n, k))