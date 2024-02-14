# 입국 심사
# 심사를 마치는데 걸리는 시간을 탐색했음
# 초기 start = 0, end = max(time) * m 로 설정하고 이분 탐색을 해나감
# 심사를 마치는데 걸리는 시간 (mid)를 각 심사관 당 걸리는 시간으로 나눈 몫을 count에 더해나간 값은 해당 시간 동안 심사할 수 있는 사람 수가 된다.
# count 값이 m보다 작을 경우에는 답이 될 가능성이 없으니 mid값을 늘려주기 위해 start값을 mid+1로 변경해준다.
# count 값이 m보다 크거나 같을 경우에는 답이 될 가능성이 있는 경우다.
# 이 경우에는 mid값을 줄여나가면서 더 작은 정답이 존재하는지 탐색해준다.


n, m = map(int, input().split())
time = [int(input()) for _ in range(n)]
time.sort()

start = 0
end = time[-1] * m
answer = -1

while start <= end:
    mid = (start + end) // 2
    count = 0
    for t in time:
        count += mid//t
    if count >= m:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)