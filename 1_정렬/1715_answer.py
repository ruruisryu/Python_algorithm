#힌트를 보고 다시 푼 버전
import heapq

n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)

result = 0

if(n == 1):
    print(0)
else:
    # 우선순위 큐가 빌 때까지 while문을 반복
    # 파이썬은 if문에서 empty list는 False를, empty가 아닌 list는 True를 리턴
    while len(heap) != 1:
        add_tmp = heapq.heappop(heap) + heapq.heappop(heap)
        heapq.heappush(heap, add_tmp)
        result += add_tmp
    print(result)