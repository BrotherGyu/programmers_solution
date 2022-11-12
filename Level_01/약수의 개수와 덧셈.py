## https://school.programmers.co.kr/learn/courses/30/lessons/77884
"""
문제 설명
두 정수 left와 right가 매개변수로 주어집니다.
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고,
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예
left	right	result
13	17	43
24	27	52
"""
def div(n):
    li=[]
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            li.append(i) 
            if ( (i**2) != n) : 
                li.append(n // i)
    return -1 if len(li)%2!=0 else 1

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer+=i*div(i)
    return answer