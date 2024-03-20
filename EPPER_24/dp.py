#피보나치 DP

# 메모이제이션 (탑다운)
d = [0] * 100
def fibo_topdown(x):
    if x is 2 or x is 1:
        return 1
    if d[x] is not 0:
        return d[x]

    d[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
    return d[x]

print(fibo_topdown(99))


# 바텀업
d = [0] * 100
d[1] = 1
d[2] = 1

def fibo_bottomup(x):
    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]

print(fibo_bottomup(99))

