## https://school.programmers.co.kr/learn/courses/30/lessons/43105
## 동적계획법(Dynamic Programming)
"""
문제 설명
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5     

위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

제한사항
삼각형의 높이는 1 이상 500 이하입니다.
삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
입출력 예
triangle	result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30
"""
## 보텀업 다이나믹 프로그래밍
def solution(triangle):
    for x in range(len(triangle)-1,0,-1):
        for y in range(x):
            a=triangle[x-1][y]+triangle[x][y]
            b=triangle[x-1][y]+triangle[x][y+1]
            triangle[x-1][y]=max(a,b)
    answer = triangle[0][0]
    return answer
"""
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.06ms, 10.2MB)
테스트 4 〉	통과 (0.34ms, 10.1MB)
테스트 5 〉	통과 (1.31ms, 10.3MB)
테스트 6 〉	통과 (0.37ms, 10.2MB)
테스트 7 〉	통과 (1.27ms, 10.1MB)
테스트 8 〉	통과 (0.28ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉통과 (0.17ms, 10.2MB)

효율성  테스트
테스트 1 〉	통과 (44.41ms, 13.9MB)
테스트 2 〉	통과 (31.36ms, 13MB)
테스트 3 〉	통과 (46.35ms, 14.5MB)
테스트 4 〉	통과 (45.19ms, 14.2MB)
테스트 5 〉	통과 (38.11ms, 14MB)
테스트 6 〉	통과 (52.34ms, 14.4MB)
테스트 7 〉	통과 (48.35ms, 14.4MB)
테스트 8 〉	통과 (39.05ms, 13.5MB)
테스트 9 〉	통과 (37.88ms, 13.7MB)
테스트 10 〉통과 (44.34ms, 14.4MB)
"""