#골드바흐 파티션
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return primes
T= int(input())

max_N=0
test_case=[]
for _ in range(T):
     N=int(input())
     test_case.append(N)
     max_N=max(max_N,N)
prime_up_to_max_N=sieve_of_eratosthenes(max_N)

for N in test_case:
        count_gold=0
        for prime in range(2, N//2+1):
             if prime_up_to_max_N[prime] and prime_up_to_max_N[N-prime]:
                count_gold+=1
        print(count_gold)
