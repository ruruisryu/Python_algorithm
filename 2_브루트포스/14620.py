from itertools import combinations

n = int(input())

flower = [list(map(int, input().split())) for _ in range(n)]
# 씨앗을 심을 수 있는 좌표 리스트
pos = [(r,c) for r in range(1, n-1) for c in range(1, n-1)]
# pos의 성분 3개로 만들 수 있는 조합(튜플)을 리스트로 변환
candidates = list(combinations(pos, 3))

# 한 좌표에 씨앗을 심기 위해 필요한 비용 계산 함수
def get_cost(pos):
    return flower[pos[0]][pos[1]] + flower[pos[0]+1][pos[1]] + flower[pos[0]-1][pos[1]] + flower[pos[0]][pos[1]+1] + flower[pos[0]][pos[1]-1]

min_cost = 99999
# 좌표 상에서 같은 거리에 떨어져 있는 점들의 규칙을 잘 생각해보기
# 알튜비튜 힌트: 3칸 중 어떤 두 칸 (r1,c1), (r2,c2)가 abs(r1 - r2) + abs(c1 - c2) <= 2 인 경우를 제외시키면 됩니다.
for i in candidates:
    if((abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])) <=2):
        continue
    if((abs(i[0][0] - i[2][0]) + abs(i[0][1] - i[2][1])) <=2):
        continue
    if((abs(i[2][0] - i[1][0]) + abs(i[2][1] - i[1][1])) <=2):
        continue
    min_cost = min(min_cost, get_cost(i[0]) + get_cost(i[1]) + get_cost(i[2]))

print(min_cost)




