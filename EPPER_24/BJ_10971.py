# 외판원 순회2

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
answer = 100000000
total_weight = 0
is_visited = [False] * n

def backtrack(cnt, before):
    global answer, total_weight, is_visited
    # 종료조건
    # 모든 도시를 순회한 시점
    # -> 마지막 도시에서 첫 도시로 갈 수 있을 경우 answer 업데이트
    # -> 그렇지 않을 경우 그냥 return해 가지치기
    if cnt == n-1 and w[before][0] != 0:
        answer = min(answer, total_weight + w[before][0])
        return
    if cnt == n-1 and w[before][0] == 0:
        return

    for i in range(0, n):
        if is_visited[i] is True or w[before][i] == 0:
            continue
        else:
            total_weight += w[before][i]
            is_visited[i] = True
            backtrack(cnt+1, i)
            total_weight -= w[before][i]
            is_visited[i] = False


# 한 사이클을 만들면, 어느 도시에서 시작하든 값은 같으므로 0번 도시부터 시작하는 경우만 검사하면 된다. <--- hint 봤음!
is_visited[0] = True
backtrack(0, 0)
print(answer)