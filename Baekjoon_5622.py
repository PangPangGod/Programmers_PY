#Baekjoon 5622 다이얼
import sys
word_to_number = {}

for idx,word in enumerate(['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'],3):
    for i in word :
        word_to_number[i] = idx

answer = 0

for i in sys.stdin.readline().rstrip() :
    answer += word_to_number[i]
print(answer)