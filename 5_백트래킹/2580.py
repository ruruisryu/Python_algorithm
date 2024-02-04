# 스도쿠
board = [list(map(int,input().split())) for _ in range(9)]
empty = []

def sudoku(count):
    global empty
    # count가 empty의 길이가 됐다면 스도쿠의 모든 칸을 다 채웠다는 의미이므로 답을 print해준뒤 종료해준다.
    if count == len(empty):
        for i in board:
            print(*i)
        exit()

    # 현재 empty 속 count 인덱스에 해당하는 칸에 1부터 9까지 넣을 수 있는 경우에 대해 가지를 뻗어나간다.
    for i in range(1, 10):
        x = empty[count][0]
        y = empty[count][1]
        another_empty = False
        for j in range(9):
            # 가로줄, 세로줄, 사각 박스를 체크해 i에 해당하는 숫자가 모두 존재하지 않는다면 현재 칸에는 i를 넣을 수 있다는 뜻이다
            # 가로줄 체크
            if board[x][j] == i:
                another_empty = True
                break
            # 세로줄 체크
            if board[j][y] == i:
                another_empty = True
                break
            # 사각 박스 체크
            if board[j%3 + x//3 * 3][j//3 + y//3 * 3] == i:
                another_empty = True
                break

        # another_empty가 True일 경우 가지치기
        if another_empty is False:
            # 현재 칸을 i로 채우고 다음 칸을 채우는 과정 이어서 진행
            board[x][y] = i
            sudoku(count+1)
            # 반납
            board[x][y] = 0

# 빈 칸의 위치 찾아서 empty 리스트에 넣어주기
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty.append((i,j))
sudoku(0)