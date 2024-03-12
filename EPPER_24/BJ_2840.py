#행운의 바퀴
n, k = map(int, input().split())
inputs = [input().split() for _ in range(k)]
answer = ['?'] * n
d = {}

count = 0
for input in inputs:
    count += int(input[0])
    # 해당 칸이 이미 다른 알파벳으로 채워져있다면
    if answer[count%n] != '?' and answer[count%n] != input[1]:
        print('!');
        exit()
    # 이미 사용된 알파벳이라면 !
    if d.get(input[1]) is not None and d.get(input[1])!= count%n:
        print('!')
        exit()
    answer[count%n] = input[1]
    # 딕셔너리에 해당 알파벳을 사용했다고 기록
    d[input[1]] = count%n


for i in range(n):
    print(answer[(count-i)%n], end="")

