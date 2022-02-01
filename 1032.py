# 파일 개수 입력 받음
N = int(input())
# 첫번째 파일의 이름을 리스트 형태로 방아서 저장
first_word = list(input())
# 첫번째 파일의 이름의 길이를 저장
first_word_len = len(first_word)
             
for i in range(N - 1):
    other_words = list(input())
    for j in range(first_word_len):
        # 다른점이 보이면
        if first_word[j] != other_words[j]:
            # '?'로 대체
            first_word[j] = '?'

print(''.join(first_word))