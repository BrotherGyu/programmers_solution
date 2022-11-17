import heapq
## https://docs.python.org/ko/3/library/heapq.html

## 힙 정렬
def heapsort(iterable):
    h = iterable
    ## 아래와 똑같은 방법 - 리스트를 힙으로 변환
    heapq.heapify(h)
    #for value in iterable:
    #    heapq.heappush(h, value)
    print(h)
    return [heapq.heappop(h) for i in range(len(h))]

## 최대 힙
def maxheapsort(iterable):
    max_h = []
    for value in iterable:
        heapq.heappush(max_h, (-value, value))
    print(max_h)
    return [heapq.heappop(max_h)[1] for i in range(len(max_h))]

if __name__ == '__main__':
    ## 힙 정렬
    print('힙 정렬')
    print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

    ## 최대 힙
    print('최대 힙')
    print(maxheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))