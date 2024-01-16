# 사과나무
# 풀이참고: https://ye5ni.tistory.com/89
# 1. 한번 물을 뿌릴 때마다 1+2씩 자라므로 나무들의 높이 합 total은 3의 배수여야 한다.
#    이때 물을 뿌린 횟수 k는 total/3 이다.

# 2. 2물뿌리개를 k번 이상 뿌릴 수 있는 상황이 확보되어야한다.
#    왜냐하면 1물뿌리개와 2물뿌리개는 둘 다 k번 뿌리게 되는데,
#    2물뿌리개를 1번 뿌리는 것은 1물뿌리개를 2번 뿌리는 것으로 바꿀 수 있다.
#    2물뿌리개를 사용할 수 있는 횟수가 총 성장 일수보다 작다는 것은 1을 더 많이 사용해야 하는 것이라서 제시된 조건과 맞지 않다.

n = int(input())
trees = list(map(int, input().split()))

total = 0
two = 0
for tree in trees:
    total += tree
    two += tree//2

if total % 3 != 0:
    print("NO")
elif two < total/3:
    print("NO")
else:
    print("YES")