# 특정 거리의 도시 찾기
# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.
# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.

# -> BFS를 사용하면 K 깊이까지 갔을때까지만 탐색하고 끝낼 수 있지 않을까?
# -> 특정 노드와 인접한 모든 노드를 탐색해야하고, 노드의 개수가 최대 30만개로 많으니까 인접 리스트를 사용하는 것이 좋을 것 같다.
# => BFS와 인접 리스트를 사용해서 탐색 구현!

from collections import deque

#탐색
def bfs(graph, x, visited, k):
    queue = deque([x])
    visited[x] = True
    # 깊이를 저장할 리스트
    result = [0] * len(graph)
    while queue:
        node = queue.popleft()
        # 현재 pop한 노드의 깊이가 k라면 이미 k깊이까지는 모두 탐색이 완료된 상태이므로 break
        if result[node] == k:
            break
        for n in graph[node]:
            if visited[n] == False:
                visited[n] = True
                # 현재 방문하는 노드의 깊이는 부모의 깊이 + 1을 해준다
                result[n] = result[node] + 1
                queue.append(n)
    return result

# 입력
# n, m, k, x = tuple(list(map(int, input().split())))
# 위 코드 아래로 간단하게 표현 가능
n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [False] * (n+1)

result = bfs(graph, x, visited, k)

# 출력
is_result_exist = False
for i in range(1, n+1):
    if result[i] == k:
        is_result_exist = True
        print(i)

if not is_result_exist:
    print(-1)

# visited의 모든 값을 -1로 초기화하고 -1일때를 방문하지 않은 상태로 간주, 방문할 때마다 거리를 visited에 기록해주면
# visited와 result를 따로 사용할 필요가 없다