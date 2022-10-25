## https://school.programmers.co.kr/learn/courses/30/lessons/12927
## 힙(Heap)
"""
문제 설명
회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다.
야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다.
Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,
퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

제한 사항
works는 길이 1 이상, 20,000 이하인 배열입니다.
works의 원소는 50000 이하인 자연수입니다.
n은 1,000,000 이하인 자연수입니다.
입출력 예
works	n	result
[4, 3, 3]	4	12
[2, 1, 2]	1	6
[1,1]	3	0
"""
import heapq
def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return 0
    h_que=[]
    for val in works:
        heapq.heappush(h_que, -1*val)
    for _ in range(n):
        heapq.heappush(h_que,heapq.heappop(h_que)+1)
    for i in h_que:
        answer+=i**2
    return answer
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.34ms, 10.1MB)
테스트 9 〉	통과 (0.54ms, 10.3MB)
테스트 10 〉통과 (0.01ms, 10.2MB)
테스트 11 〉통과 (0.02ms, 10.1MB)
테스트 12 〉통과 (0.01ms, 10.1MB)
테스트 13 〉통과 (0.00ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (366.01ms, 9.88MB)
테스트 2 〉	통과 (378.49ms, 10.1MB)
"""