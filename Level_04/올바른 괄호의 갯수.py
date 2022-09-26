## https://school.programmers.co.kr/learn/courses/30/lessons/12929
"""
문제 설명
올바른 괄호란 (())나 ()와 같이 올바르게 모두 닫힌 괄호를 의미합니다. )(나 ())() 와 같은 괄호는 올바르지 않은 괄호가 됩니다. 괄호 쌍의 개수 n이 주어질 때, n개의 괄호 쌍으로 만들 수 있는 모든 가능한 괄호 문자열의 갯수를 반환하는 함수 solution을 완성해 주세요.

제한사항
괄호 쌍의 개수 N : 1 ≤ n ≤ 14, N은 정수
"""
import math
## 카탈란수
## Catalan(n)=2n!/(n!*(n+1)!)
def solution(n):
    return math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1))