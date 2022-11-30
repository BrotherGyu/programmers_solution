## https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
입출력 예
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
"""
from itertools import combinations
def prime(num_li):
    answer=0
    max_num_li=max(num_li)
    prime_list=[False, False] + [True] * (max_num_li-1)
    for i in range(2, max_num_li+1):
        if prime_list[i]:
            for j in range(2*i, max_num_li+1, i):
                prime_list[j] = False
    for i in num_li:
        if prime_list[i]==True:
            answer+=1
    return answer


def solution(nums):
    num_li=[]
    for i in combinations(nums,3):
        num_li.append(sum(i))
    return prime(num_li)