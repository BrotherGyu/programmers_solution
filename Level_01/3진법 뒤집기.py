## https://school.programmers.co.kr/learn/courses/30/lessons/68935
"""
문제 설명
자연수 n이 매개변수로 주어집니다.
n을 3진법 상에서 앞뒤로 뒤집은 후,
이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1 이상 100,000,000 이하인 자연수입니다.
입출력 예
n	result
45	7
125	229
"""
def conv_10to3_reverse (n):
    ans = ''
    while n > 0:
        n, mod = divmod(n, 3)
        ans += str(mod)
    return ans

def conv_3to10 (n):
    ans=0
    for index, value in enumerate(n[::-1]):
        ans+=int(value)*(3**index)
    return ans

def solution(n):
    return conv_3to10(conv_10to3_reverse(n))