## https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3
## 완전탐색
"""
문제 설명
사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

제한사항
word의 길이는 1 이상 5 이하입니다.
word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.
입출력 예
word	result
"AAAAE"	6
"AAAE"	10
"I"	1563
"EIO"	1189
"""
from collections import deque
def solution(word):
    answer = 0
    word_li=['A','E','I','O','U']
    input_word=''
    word_queue=deque()
    for i in word_li:
        input_word=i
        word_queue.append(input_word)
        
        for i_1 in word_li:
            input_word_1=input_word+i_1
            word_queue.append(input_word_1)
            
            for i_2 in word_li:
                input_word_2=input_word_1+i_2
                word_queue.append(input_word_2)
                
                for i_3 in word_li:
                    input_word_3=input_word_2+i_3
                    word_queue.append(input_word_3)
                    
                    for i_4 in word_li:
                        input_word_4=input_word_3+i_4
                        word_queue.append(input_word_4)
    answer=word_queue.index(word)+1
    return answer