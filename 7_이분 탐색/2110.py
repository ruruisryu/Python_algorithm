# 공유기 설치

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1                   # 바로 옆에 있는 경우
end = house[-1] - house[0]  # 양 끝에 있을 경우
max_distance = house[-1] - house[0]
answer = -1

while start <= end:
    mid = (start + end) // 2
    # count = max_distance // mid
    current = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]

    if count >= c :
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
