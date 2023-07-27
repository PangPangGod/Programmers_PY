#Baekjoon 5598 카이사르 암호

from collections import deque
alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
alphabet_convert = deque(alphabet[:])
alphabet_convert.rotate(-3)

alphabet_cov_dic = {}

for num,word in enumerate(alphabet_convert):
    alphabet_cov_dic[word]=num

answer = ''
for word in input() :
    answer += alphabet[alphabet_cov_dic[word]]

print(answer)