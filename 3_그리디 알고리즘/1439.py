#문자열 뒤집기
string = list(input())

# string을 돌면서 앞뒤 문자가 다를때마다 +1 해줌
count = 1
for i in range(1, len(string)):
    if string[i] == string[i-1]:
        continue
    count += 1

print(count//2)