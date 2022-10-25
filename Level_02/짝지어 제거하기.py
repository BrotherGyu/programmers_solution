## https://school.programmers.co.kr/learn/courses/30/lessons/12973
## 2017 팁스타운[스택]
"""
문제 설명
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다.
먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.
그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.
이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.
문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

제한사항
문자열의 길이 : 1,000,000이하의 자연수
문자열은 모두 소문자로 이루어져 있습니다.
입출력 예
s	result
baabaa	1
cdcd	0
"""
from collections import deque
def solution(s):
    if len(s)%2!=0:
        return 0
    s, que = deque(s),deque()
    while len(s)!=0:
        if len(que)==0:
            que.append(s.popleft())
        elif que[-1]==s[0]:
            que.pop()
            s.popleft()
        else:
            que.append(s.popleft())
    if len(que)==0:
        return 1
    return 0
"""
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (28.32ms, 10.8MB)
테스트 3 〉	통과 (26.64ms, 10.9MB)
테스트 4 〉	통과 (47.97ms, 11MB)
테스트 5 〉	통과 (27.28ms, 10.8MB)
테스트 6 〉	통과 (26.12ms, 11MB)
테스트 7 〉	통과 (38.33ms, 11.1MB)
테스트 8 〉	통과 (24.81ms, 11MB)
테스트 9 〉	통과 (0.00ms, 10.2MB)
테스트 10 〉통과 (0.04ms, 10.2MB)
테스트 11 〉통과 (0.00ms, 10.1MB)
테스트 12 〉통과 (0.00ms, 10.1MB)
테스트 13 〉통과 (0.01ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (241.43ms, 19MB)
테스트 2 〉	통과 (215.61ms, 18.6MB)
테스트 3 〉	통과 (241.58ms, 19MB)
테스트 4 〉	통과 (271.99ms, 18.8MB)
테스트 5 〉	통과 (240.66ms, 18.9MB)
테스트 6 〉	통과 (266.61ms, 18.9MB)
테스트 7 〉	통과 (295.49ms, 18.9MB)
테스트 8 〉	통과 (247.19ms, 19MB)
"""