## https://school.programmers.co.kr/learn/courses/30/lessons/60057
## 2020 KAKAO BLIND RECRUITMENT
"""
문제 설명
데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.
최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데,
문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
간단한 예로 "aabbaccc"의 경우 "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데,
이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.
예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다.
"어피치"는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만,
2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며,
이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만,
3개 단위로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다.
이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때,
위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

제한사항
s의 길이는 1 이상 1,000 이하입니다.
s는 알파벳 소문자로만 이루어져 있습니다.
입출력 예
s	result
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
"""
from collections import deque
def string_comp(s,i):
    string_dq=deque([s[ck:ck+i] for ck in range(0,len(s),i)]+[None])
    save_dq=deque()
    save_dq.append(string_dq.popleft())
    count=1
    answer=''
    while len(string_dq)!=0:
        if save_dq[0]==string_dq[0]:
            count+=1
            string_dq.popleft()
        else:
            if count==1:
                answer+=save_dq[0]
                save_dq.append(string_dq.popleft())
                save_dq.popleft()
            elif string_dq[0]==None:
                answer+=str(count)+save_dq[0]
                break
            else:
                answer+=str(count)+save_dq[0]
                save_dq.append(string_dq.popleft())
                save_dq.popleft()
            count=1
    return len(answer)
def solution(s):
    len_s=len(s)
    answer = len_s
    chk_point=1
    while chk_point<=len_s//2:
        answer=min(answer,string_comp(s,chk_point))
        chk_point+=1
    return answer
"""
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.2MB)
테스트 2 〉	통과 (0.81ms, 10.2MB)
테스트 3 〉	통과 (0.62ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (0.77ms, 10.4MB)
테스트 8 〉	통과 (0.92ms, 10.3MB)
테스트 9 〉	통과 (1.74ms, 10.3MB)
테스트 10 〉통과 (3.36ms, 10.3MB)
테스트 11 〉통과 (0.24ms, 10.4MB)
테스트 12 〉통과 (0.15ms, 10.2MB)
테스트 13 〉통과 (0.17ms, 10.2MB)
테스트 14 〉통과 (0.99ms, 10.2MB)
테스트 15 〉통과 (0.28ms, 10.3MB)
테스트 16 〉통과 (0.04ms, 10.3MB)
테스트 17 〉통과 (1.63ms, 10.2MB)
테스트 18 〉통과 (1.74ms, 10.4MB)
테스트 19 〉통과 (3.00ms, 10.2MB)
테스트 20 〉통과 (3.60ms, 10.3MB)
테스트 21 〉통과 (3.42ms, 10.2MB)
테스트 22 〉통과 (3.55ms, 10.2MB)
테스트 23 〉통과 (3.38ms, 10.2MB)
테스트 24 〉통과 (3.25ms, 10.2MB)
테스트 25 〉통과 (3.47ms, 10.4MB)
테스트 26 〉통과 (3.39ms, 10.3MB)
테스트 27 〉통과 (3.57ms, 10.4MB)
테스트 28 〉통과 (0.03ms, 10.2MB)
"""