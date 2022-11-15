import math
## 최대공약수 math.gcd(a, b)도 가능
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

## 최소 공배수
def lcm(a, b):
    return a * b / gcd(a, b)