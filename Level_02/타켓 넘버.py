## https://school.programmers.co.kr/learn/courses/30/lessons/43165
## 깊이/너비 우선 탐색(DFS/BFS)
"""
문제 설명
n개의 음이 아닌 정수들이 있습니다. 
이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서
타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
입출력 예
numbers	target	return
[1, 1, 1, 1, 1]	3	5
[4, 1, 2, 1]	4	2
"""
## DFS/BFS 사용 안하고 해결

from itertools import product
def solution(numbers, target):
    pruduct_li = list(product([-1,1], repeat=len(numbers)))
    answer = []
    for permu_li in pruduct_li:
        result = 0
        for x, y in zip(numbers, permu_li):
            result += x*y
        answer.append(result)
    return answer.count(target)

## 참고 할만한 풀이
from itertools import product
def solution(numbers, target):
    li = [(x, -x) for x in numbers]
    product_li = list(map(sum,product(*li)))
    return product_li.count(target)