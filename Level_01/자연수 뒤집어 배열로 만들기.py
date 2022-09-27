## https://school.programmers.co.kr/learn/courses/30/lessons/12932
"""
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
"""
def solution(n):
    answer=[]
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer

"""
def solution(n):
    answer=[]
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer
"""