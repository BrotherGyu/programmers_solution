## https://school.programmers.co.kr/learn/courses/30/lessons/118667#
## 스택/큐
"""
문제 설명
길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고,
추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다.
이때 필요한 작업의 최소 횟수를 구하고자 합니다. 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.

큐는 먼저 집어넣은 원소가 먼저 나오는 구조입니다. 이 문제에서는 큐를 배열로 표현하며,
원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다.
즉, pop을 하면 배열의 첫 번째 원소가 추출되며, insert를 하면 배열의 끝에 원소가 추가됩니다.
예를 들어 큐 [1, 2, 3, 4]가 주어졌을 때, pop을 하면 맨 앞에 있는 원소 1이 추출되어 [2, 3, 4]가 되며,
이어서 5를 insert하면 [2, 3, 4, 5]가 됩니다.

다음은 두 큐를 나타내는 예시입니다.

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
두 큐에 담긴 모든 원소의 합은 30입니다. 따라서, 각 큐의 합을 15로 만들어야 합니다. 예를 들어, 다음과 같이 2가지 방법이 있습니다.

queue2의 4, 6, 5를 순서대로 추출하여 queue1에 추가한 뒤, queue1의 3, 2, 7, 2를 순서대로 추출하여 queue2에 추가합니다.
그 결과 queue1은 [4, 6, 5], queue2는 [1, 3, 2, 7, 2]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 7번 수행합니다.
queue1에서 3을 추출하여 queue2에 추가합니다. 그리고 queue2에서 4를 추출하여 queue1에 추가합니다.
그 결과 queue1은 [2, 7, 2, 4], queue2는 [6, 5, 1, 3]가 되며, 각 큐의 원소 합은 15로 같습니다.
이 방법은 작업을 2번만 수행하며, 이보다 적은 횟수로 목표를 달성할 수 없습니다.
따라서 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수는 2입니다.

길이가 같은 두 개의 큐를 나타내는 정수 배열 queue1, queue2가 매개변수로 주어집니다.
각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요.
단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.

제한사항
1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
1 ≤ queue1의 원소, queue2의 원소 ≤ 109
주의: 언어에 따라 합 계산 과정 중 산술 오버플로우 발생 가능성이 있으므로 long type 고려가 필요합니다.
입출력 예
queue1	queue2	result
[3, 2, 7, 2]	[4, 6, 5, 1]	2
[1, 2, 1, 2]	[1, 10, 1, 2]	7
[1, 1]	[1, 5]	-1
"""
from collections import deque
def solution(queue1, queue2):
    queue1, queue2=deque(queue1),deque(queue2)
    len_queue=len(queue1)+len(queue2)
    answer=0
    queue1_sum, queue2_sum=sum(queue1), sum(queue2)
    while len_queue*3>=answer:
        if queue1_sum==queue2_sum:
            return answer
        elif queue1_sum>queue2_sum:
            value=queue1.popleft()
            queue2.append(value)
            queue1_sum, queue2_sum = queue1_sum-value,queue2_sum+value
        else:
            value=queue2.popleft()
            queue1.append(value)
            queue1_sum, queue2_sum = queue1_sum+value,queue2_sum-value
        answer+=1
    return -1
"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.03ms, 10MB)
테스트 7 〉	통과 (0.03ms, 10.1MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉통과 (0.11ms, 10.2MB)
테스트 11 〉통과 (70.31ms, 14.7MB)
테스트 12 〉통과 (6.94ms, 14.6MB)
테스트 13 〉통과 (4.31ms, 12.1MB)
테스트 14 〉통과 (2.52ms, 12.3MB)
테스트 15 〉통과 (6.07ms, 18MB)
테스트 16 〉통과 (3.60ms, 18.4MB)
테스트 17 〉통과 (3.27ms, 17.6MB)
테스트 18 〉통과 (17.77ms, 33.2MB)
테스트 19 〉통과 (13.82ms, 37.3MB)
테스트 20 〉통과 (30.14ms, 37.6MB)
테스트 21 〉통과 (19.38ms, 37.6MB)
테스트 22 〉통과 (60.89ms, 37.8MB)
테스트 23 〉통과 (47.16ms, 37.9MB)
테스트 24 〉통과 (66.86ms, 37.9MB)
테스트 25 〉통과 (0.05ms, 10.1MB)
테스트 26 〉통과 (0.03ms, 10.1MB)
테스트 27 〉통과 (0.04ms, 10.1MB)
테스트 28 〉통과 (130.49ms, 19.4MB)
테스트 29 〉통과 (0.56ms, 10.8MB)
테스트 30 〉통과 (48.31ms, 19.4MB)
"""