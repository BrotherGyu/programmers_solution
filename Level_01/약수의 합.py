## https://school.programmers.co.kr/learn/courses/30/lessons/12928
"""
문제 설명
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

제한 사항
n은 0 이상 3000이하인 정수입니다.
"""
import math
def solution(n):
    answer = 0
    if n==0 or n==1:
        return n
    n_sqrt=math.sqrt(n)
    for i in range(1,int(n_sqrt+1)):
        if i*(n//i)==n:
            answer+=i+(n//i)
    if int(n_sqrt)**2==n:
        answer-=n_sqrt
    return answer