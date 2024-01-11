n = int(input())
candy = [list(input()) for _ in range(n)]
max_candy = 1

# 열 하나하나를 돌며 같은 숫자가 연이어 나오는 횟수를 max_candy와 계산한다
def check(candies):
    global max_candy
    for candy in candies:
        temp_max_candy = 1
        for i in range(n-1):
            if(candy[i+1] == candy[i]):
                temp_max_candy += 1
            else:
                max_candy = max(max_candy, temp_max_candy)
                temp_max_candy = 1
        max_candy = max(max_candy, temp_max_candy)

# 원 상태의 캔디 체크
check(candy)
check(zip(*candy))

for i in range(n):
    for j in range(n):
        # 캔디의 위치가 맨 끝이 아니고, 인접한 두 캔디의 색이 다를 때
        # 세로 방향 바꾸기
        if(i != n-1 and candy[i][j] != candy[i+1][j]):
            # 인접한 두 캔디의 위치를 바꾼다
            candy [i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            # 바꾼 상태에서 가장 많이 먹을 수 있는 캔디의 개수를 세고 max값과 비교해 업데이트
            check(candy)
            check(zip(*candy))
            # 캔디의 위치를 원래 상태로 바꾸어준다
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
        # 가로 방향 바꾸기
        if(j != n-1 and candy [i][j] != candy[i][j+1]):
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            check(candy)
            check(zip(*candy))
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

print(max_candy)