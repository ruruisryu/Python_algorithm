# 팰린드롬 만들기
# dict 사용 버전
name = list(input())
dict = {}

# 각 단어가 몇번 나오는지 '단어: 개수' 형태로 dict에 넣음
for word in name:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

# 홀수개 단어가 2개 이상이라면 팰린드롬을 만들지 못한다
# 홀수개 단어의 개수 세주기
even = ""
count = 0
for key in dict.keys():
    if dict[key]%2 == 1:
        even = key
        count += 1
    if count > 1:
        print("I'm Sorry Hansoo")
        exit()

# 사전순으로 팰린드롬 만들기
dict = sorted(dict.items())
result = ""
for item in dict:
    result += item[0] * (item[1]//2)

# 결과 출력
print(f"{result}{even}{result[::-1]}")