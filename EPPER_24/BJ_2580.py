#스도쿠
SIZE = 9
empty = []
answer = []

def is_right_num(num, i, j):
    for idx in range(SIZE):
        # 가로줄 체크
        if answer[i][idx] == num:
            return False
        # 세로줄 체크
        if answer[idx][j] == num:
            return False
        # 네모칸 체크
        if answer[(i//3) + (idx%3)][(j//3) + (idx%3)] == num:
            return False
    return True

def backtrack(cnt):
    global empty, answer
    # 종료조건: cnt가 빈칸 개수(empty 사이즈)만큼일때
    if cnt == len(empty):
        return

    for i in range(1, 10):
        x = empty[cnt][0]
        y = empty[cnt][1]
        # 가로줄, 세로줄, 같은 칸에 동일한 숫자가 없을 경우
        if is_right_num(i, x, y):
            answer[x][y] = i
            backtrack(cnt+1)
            answer[x][y] = 0

def solution(sudoku):
    answer = sudoku
    for i in range(SIZE):
        for j in range(SIZE):
            if sudoku[i][j] == 0:
                empty.append([i , j])
    backtrack(0)
    return answer

#----------------------------------------------------------------------
if __name__ == "__main__":
    # 입력
    sudoku = [list(map(int, input().split())) for _ in range(SIZE)]

    # 연산 & 출력
    for line in solution(sudoku):
        print(*line)
        # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
        # print(*[1, 2, 3]) == print(1, 2, 3)