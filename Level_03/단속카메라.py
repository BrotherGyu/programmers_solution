## https://school.programmers.co.kr/learn/courses/30/lessons/42884
## 탐욕법(Greedy)
"""
문제 설명
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

제한사항

차량의 대수는 1대 이상 10,000대 이하입니다.
routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점,
routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.
입출력 예

routes	return
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	2
입출력 예 설명

-5 지점에 카메라를 설치하면 두 번째, 네 번째 차량이 카메라를 만납니다.

-15 지점에 카메라를 설치하면 첫 번째, 세 번째 차량이 카메라를 만납니다.
"""
from collections import deque
def solution(routes):
    answer = 0
    end_point=-30001
    routes.sort(key=lambda x:(x[1],x[0]))
    routes=deque(routes)
    while True:
        try:
            output_li=routes.popleft()
            if output_li[0]<=end_point and end_point<=output_li[1]:
                pass
            else:
                end_point=output_li[1]
                answer+=1
        except:
            return answer
"""
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (0.88ms, 10.5MB)
테스트 2 〉	통과 (0.62ms, 10.3MB)
테스트 3 〉	통과 (1.95ms, 10.6MB)
테스트 4 〉	통과 (0.15ms, 10.2MB)
테스트 5 〉	통과 (2.75ms, 10.9MB)
"""