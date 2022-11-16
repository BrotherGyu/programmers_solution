import math

def prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    print(prime_number(7))
    print(prime_number(6))
    print(prime_number(397))

"""
## 출처 : 코딩으로 수학하기 [https://wikidocs.net/21638]
에라토스테네스의 체 : 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법.
-- 범위의 모든 소수를 구할 때는 효율적인 방법
1. 1은 제거
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택하고, 나머지 2의 배수를 모두 지운다.
3. 지워지지 않은 수 중 제일 작은 3을 소수로 채택하고, 나머지 3의 배수를 모두 지운다.
4. 지워지지 않은 수 중 제일 작은 5를 소수로 채택하고, 나머지 5의 배수를 모두 지운다.
5. (반복)
"""
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)
