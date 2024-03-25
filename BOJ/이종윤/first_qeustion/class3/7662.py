#이중 우선순 큐
import heapq
import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    max_heap, min_heap=[], []
    visit=[False]*1000001
    K=int(input())
    for key in range(K):
        order=input().rsplit()
        # 값 추가
        if order[0]=='I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1])*-1, key)) #최대힙의 경우는 최소힙의 -를 씌워서 표출한다.
            visit[key] =True
        elif order[0]=='D':
            #최소값 삭제
            if order[1] =='-1':
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] =False
                    heapq.heappop(min_heap)
            # 최대값 삭제
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]]=False
                    heapq.heappop(max_heap)
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap) 
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')