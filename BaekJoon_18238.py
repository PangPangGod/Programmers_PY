import string
words = list(string.ascii_uppercase)

current_index = 0
answer = 0
ZOAC = list(input())

for i in ZOAC :
    left=len(words)-abs(current_index-words.index(i))
    right=current_index-words.index(i)
    answer += min(abs(left),abs(right))
    current_index = words.index(i)
print(answer)