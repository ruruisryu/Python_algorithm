BOARD_SIZE = 19

board = [input().split() for _ in range(BOARD_SIZE)]

# 입력으로 들어온 인덱스가 board를 벗어나는지 체크
# 벗어났다면 True리턴
def check_indexOutOfBoard(i, j):
    if(i < 0 or i >= BOARD_SIZE or j < 0 or j >= BOARD_SIZE):
        return True
    return False

def check_winner(i, j):
    global board, winner
    # 우, 하, 우하, 우상 4가지 방향에 대한 인덱스
    direction = [(0,1), (1,0), (1,1), (-1, 1)]
    for di, dj in direction:
        ni, nj = i + di, j + dj
        count = 1
        # 한방향으로 4번 전진. 만약 도중에 보드 바깥으로 나가거나 기준점과 다른 색의 바둑알이 있다면
        # 오목이 될 가능성이 0이므로 현재 방향에 대한 탐색을 그만둔다.
        for k in range(1, 5):
            if(check_indexOutOfBoard(ni, nj) or board[ni][nj] != board[i][j]):
                break
            else:
                ni, nj = ni + di, nj + dj
                count += 1

        # 같은 바둑알이 연속으로 5개 있지 않다면 다음 경우의 수를 체크
        if(count != 5):
            continue
        # 같은 방향으로 한 번 더 갔을때 같은 색 바둑돌이 있다면 오목이 아니라 6목이므로 다음 경우의 수를 체크
        if(not check_indexOutOfBoard(ni, nj) and board[ni][nj] == board[i][j]):
            continue
        # 기준점에서 반대 방향으로 한 번 갔을 때 같은 색 바둑돌이 있다면 오목이 아니라 6목이므로 다음 경우의 수를 체크
        if(not check_indexOutOfBoard(i-di, j - dj) and board[i-di][j-dj] == board[i][j]):
            continue
        print(f"{board[i][j]}\n{i+1} {j+1}")
        exit()

for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if (board[i][j] != '0'):
            check_winner(i, j)

print('0')