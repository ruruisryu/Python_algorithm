# 인구 이동
# BFS든 DFS든 상관없을 것 같다. 문제 특성상 인접 행렬로 푸는게 나을듯
from collections import deque

n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(n)] for _ in range(n)]
dir = [(1,0), (-1,0), (0,-1), (0,1)] # 상하좌우 방향
union=[]
day = 0

# graph내에 존재하는지 체크하는 함수
def is_in_graph(node):
    if node[0] < 0 or node[0] >= n:
        return False
    if node[1] < 0 or node[1] >= n:
        return False
    return True

def bfs(graph, node, visited, union):
    queue = deque([node])
    visited[node[0]][node[1]] = True
    while queue:
        node = queue.popleft()
        for d in dir:
            new = (node[0] + d[0], node[1] + d[1])
            if not is_in_graph(new) :
                continue
            if visited[new[0]][new[1]] == True:
                continue
            deference = abs(graph[node[0]][node[1]] - graph[new[0]][new[1]])
            if l <= deference and deference <= r:
                visited[new[0]][new[1]] = True
                queue.append(new)
                union[len(union)-1].append(new)

while len(union) != 1:
    union = []
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue
            # 탐색 시작
            union.append([(i,j)])
            bfs(population, (i,j), visited, union)

    if len(union) == n * n:
        break

    day += 1
    for i in range(len(union)):
        average = 0
        for nation in union[i]:
            average += population[nation[0]][nation[1]]
        average = average // len(union[i])
        for nation in union[i]:
            population[nation[0]][nation[1]] = average

print(day)