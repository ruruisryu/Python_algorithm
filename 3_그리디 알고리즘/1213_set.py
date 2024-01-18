# 팰린드롬 만들기
# set 사용 버전
name = list(input())
keys = set(name)

count = 0
even = result = ""

for key in keys:
    if name.count(key) % 2 == 1:
        even = key
        count += 1
    if count > 1:
        print("I'm Sorry Hansoo")
        exit()

keys = sorted(list(keys))
for item in keys:
    result += item * (name.count(item)//2)

print(f"{result}{even}{result[::-1]}")