import collections

def solution(n):
    li = [i for i in range(n)]
    # deque
    que = collections.deque(li)
    print(que,'\n')

    # 첫번째 인덱스 값 추가 .appendleft()
    que.appendleft(-1)
    print('appendleft -1')
    print(que,'\n')

    # 마지막 인덱스 값 추가 .append()
    que.append(4)
    print('append 4')
    print(que,'\n')


    #첫번째 인덱스 값 삭제 .popleft()
    que.popleft()
    print('popleft')
    print(que,'\n')

    # 마지막 인덱스 값 삭제 .pop()
    que.pop()
    print('pop')
    print(que,'\n')

    # 우측 iterable 추가 .extend()
    que_1=collections.deque([3,4,5])
    que.extend(que_1)
    print('extend')
    print(que,'\n')

    # 좌측 iterable 추가 .extend()
    que_0=collections.deque([-3,-2,-1])
    que.extendleft(que_0)
    print('extendleft')
    print(que,'\n')

    # 값 회전 .rotate()
    que.rotate(1)
    print('rotate 1')
    print(que)

    que.rotate(-1)
    print('rotate -1')
    print(que,'\n')

    # 모든 요소 삭제 .clear()
    que.clear()
    print('clear')
    print(que,'\n')

    # count(i) i의 개수 반환
    que=collections.deque([1,2,2,3,3,3,4,4,4,4])
    print(que)
    print('count 1')
    print(que.count(1))
    print('count 2')
    print(que.count(2))
    print('count 3')
    print(que.count(3))

if __name__ == '__main__':
    solution(3)
