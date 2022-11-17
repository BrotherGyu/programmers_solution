import queue

## 우선순위큐의 put(), get() 함수들은 O(log n)의 시간복잡도

que = queue.PriorityQueue()
## que 사이즈 설정
#que = queue.PriorityQueue(maxsize = 8)

## que에 값추가
input_li=[3,2,1,0,-1,-2,-3]
for input_val in input_li:
    que.put(input_val)

## que 사이즈 리턴
print(que.qsize())
## que가 비었는지
print(que.empty())
## que가 가득 찼는지
print(que.full())

## 모든값 리턴
print([que.get() for _ in range(que.qsize())])
print('남은 값 개수 :',que.qsize())