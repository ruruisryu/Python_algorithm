#신입 사원
n = int(input())

for i in range(n):
    m = int(input())
    # 공백으로 구분된 숫자를 여러 줄 입력받아 각각을 int형으로 변환시키는 코드
    employee = [list(map(int, input().split())) for _ in range(m)]
    employee.sort(key=lambda x: x[0])

    result = 1
    min = employee[0][1]
    for i in range(1, m):
        if(employee[i][1] < min):
            result += 1
            min = employee[i][1]
    print(result)