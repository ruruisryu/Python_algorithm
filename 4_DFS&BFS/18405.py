# 경쟁적 전염
# 문제 특성상 BFS, 인접 행렬로 구현해야할 것 같음
from collections import deque

# 입력
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

depth = [[0 for _ in range(n)] for _ in range(n)] # 깊이를 저장할 2차원 리스트
dir = [(1,0), (-1,0), (0,-1), (0,1)] # 상하좌우 방향
virus = [] # 바이러스 근원지의 위치를 저장할 리스트

# 바이러스 근원지 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
           virus.append([graph[i][j], (i, j)])

# 수가 가장 작은 virus부터 탐색할 수 있도록 정렬해준다.
virus.sort()

# graph내에 존재하는지 체크하는 함수
def is_in_graph(node):
    if node[0] < 0 or node[0] >= n:
        return False
    if node[1] < 0 or node[1] >= n:
        return False
    return True

# 탐색
queue = deque([virus[i][1] for i in range(len(virus))])
while queue:
    node = queue.popleft()
    # 만약 이번에 pop한 노드의 깊이가 s라면 s초까지의 탐색이 완료됐고, s+1초의 탐색을 시작할 타이밍이니 break
    if depth[node[0]][node[1]] == s:
        break
    for d in dir:
        new = (node[0]+d[0], node[1]+d[1])
        # 상하좌우를 탐색, 만약 graph 바깥으로 나가게 된다면 탐색 pass
        if not is_in_graph(new):
            continue
        if graph[new[0]][new[1]] == 0:
            graph[new[0]][new[1]] = graph[node[0]][node[1]]
            depth[new[0]][new[1]] = depth[node[0]][node[1]] + 1
            queue.append(new)
# 출력
print(graph[x-1][y-1])