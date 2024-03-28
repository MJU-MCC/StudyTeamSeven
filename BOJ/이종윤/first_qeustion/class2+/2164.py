#카드 2

# n장의 카드
# 제일 위에 있는 카드 버리고 제일 위에 있는 카드를 맨 밑에 둔다.
# deque를 사용하면 list보다 빠르다(시간복잡도: O(1))

from collections import deque
n=int(input())
num_list=deque(range(1, n+1))
while len(num_list)>1:
    num_list.popleft()
    num_list.append(num_list.popleft())
print(num_list[0])