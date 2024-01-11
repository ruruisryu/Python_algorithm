#암호 만들기
from itertools import combinations

l, c = tuple(list(map(int,input().split())))        # l,c 받기
char = set(input().split())                         # 사용될 알파벳 입력 받기
candidates = list(combinations(char, l))            # 입력받은 알파벳 중 l개의 조합 리스트를 구한다
                                                    # 순열을 사용하지 않는 이유: 어차피 똑같은 종류로 이루어진 문자열들은 
                                                    # 정렬되어야한다는 조건때문에 결국 하나의 문자열로 바뀐다.   
                                                    
vowels = { 'a', 'e', 'i', 'o', 'u'}                 # 모음 집합
answers = []                                        # 정답을 담을 리스트                

# for 문을 돌면서 조건에 해당하는 문자열들만 정렬한 뒤 정답 리스트에 옭긴다.
for candidate in candidates:
    vowels_in_word = vowels & set(candidate)
    if(len(vowels_in_word) >= 1 and len(candidate) - len(vowels_in_word) >= 2):
        candidate = sorted(candidate)
        candidate = ''.join(candidate)
        answers.append(candidate)

# 정답 리스트 내의 문자열들을 정렬해준 뒤 출력
answers.sort()
for answer in answers:
    print(answer)