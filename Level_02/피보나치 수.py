## https://school.programmers.co.kr/learn/courses/30/lessons/12945
## Bottom_Up Approach
## 참고[다이나믹 프로그래밍] - https://youtu.be/vYquumk4nWw
"""
문제 설명
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.
입출력 예
n	return
3	2
5	5
입출력 예 설명
피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.
"""
## (A+B)%C=((A%C)+(B%C))%C
def solution(n):
    if n==1 or n==2:
        return 1
    answer=[0]*(n+1)
    answer[1],answer[2]=1,1
    for i in range(3,n+1):
        answer[i]=(answer[i-1]%1234567+answer[i-2]%1234567)%1234567
    return answer[n]