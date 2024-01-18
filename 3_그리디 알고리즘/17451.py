#평행우주
# 속도를 낮출 수만 있을 뿐 높일 수는 없으므로 마지막 행성으로 부터 처음 행성까지 오면서 최소 속도를 올려준다.
import math

n = int(input())
velocities = list(map(int, input().split()))
velocities.reverse()
min = velocities[0]

for i in range(1, n):
    # min과 velocities[i]일 때는 math.ceil(min / velocities[i])이 0이 되므로, continue
    # 애초에 이 경우에는 min값을 업데이트해주지 않아도 된다.
    if min == velocities[i]:
        continue
    # min값을 'min보다 큰 다음 행성의 속도의 배수중 최솟값으로 바꾸어 준다.
    min = velocities[i] * math.ceil(min / velocities[i])

print(min)

