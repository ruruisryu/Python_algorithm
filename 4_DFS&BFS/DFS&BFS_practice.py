from collections import deque

# dfs 연습
def dfs_recursive(graph, node, visited):
    # 현재 방문한 노드 방문체크해주기
    # 방문했다고 알리기 위해 print
    visited[node] = True
    print(node, end= " ")

    # 인접한 노드를 돌면서 방문하지 않은 노드가 있다면 방문
    # 더이상 방문하지 않은 인접 노드가 없다면 자연스럽게 return
    for n in graph[node]:
        if visited[n] == False:
            dfs_recursive(graph, n, visited)

graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
visited = [False] * 9
dfs_recursive(graph, 1, visited)

print()
# bfs 연습
def bfs_queue(graph, node, visited):
    # 큐 생성하고 첫 노드 넣어주기
    # 첫 노드 방문체크 해주기
    queue = deque([node])
    visited[node] = True

    # 큐가 빌 때까지 반복
    while len(queue) != 0:  # while queue: 로 대체 가능
        # 큐에서 노드 하나 pop한뒤 출력
        node = queue.popleft()
        print(node, end=" ")
        # 해당 노드와 연결되어 있는 모든 노드를 탐색하면서
        # 방문하지 않은 노드가 있다면 큐에 넣어준다 (방문 체크 필수)
        for n in graph[node]:
            if visited[n] == False:
                visited[n] = True
                queue.append(n)

graph = [[], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7]]
visited = [False] * 9
bfs_queue(graph, 1, visited)