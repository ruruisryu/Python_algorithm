#틀린 버전
n = int(input())
cards = [int(input()) for _ in range(n)]
cards.sort()

if(n == 1):
    print(0)
else:
    result = 0
    temp = cards[0]
    for i in range(n-1):
        temp += cards[i+1]
        result += temp

    print(result)

