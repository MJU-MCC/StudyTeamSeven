#뱀과 사다리 게임
# 그래프 이론중 하나인 bfs로 풀어야한다.
from collections import deque

def roll_the_dice_less(ladders, snakes):
    board=build_board(ladders,snakes)
    queue=deque([(1, 0)]) #위치, 던지는 수
    visited=[False]*101
    visited[1]=True
    while queue:
        location, throw_num=queue.popleft()
        if location==100:
            return throw_num
        for i in range(1,7):
            next_location=location+i
            if next_location<=100 and not visited[next_location]:
                visited[next_location]=True
                if board[next_location]:
                    next_location=board[next_location]
                queue.append((next_location,throw_num+1))
    return -1
def build_board(ladders, snakes):
    board=[0]*101
    for start, end in ladders:
        board[start]=end
    for start, end in snakes:
        board[start]=end 
    return board
snakes=[]
ladders=[]
n,m=map(int, input().split())
for _ in range(n):
    a,b= map(int, input().split())
    ladders.append((a,b))
for _ in range(m):
    a,b= map(int, input().split())
    snakes.append((a,b))
min=roll_the_dice_less(ladders, snakes)
print(min)