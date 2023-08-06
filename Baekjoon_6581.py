#6581 HTML
from collections import deque

def tag_br(sentence) :
    if sentence :
        print(" ".join(sentence),end="")
        sentence = []
    print()
    return sentence

def tag_hr(sentence) :
    if sentence :
        print(" ".join(sentence))
        sentence = []
    print(f"{'-'*80}")
    return sentence


def tag_cmd(cmd,sentence) :
    cmd_dic = {
        "<br>" : tag_br,
        "<hr>" : tag_hr
    }
    sentence_transformed = cmd_dic[cmd](sentence)
    return sentence_transformed


#main
word_storage = deque([])

while True:
    try:
        word_storage.extend(input().split())
    except EOFError:
        break

#공백으로 나눈 이후에 다음 기준대로 실시한다.
# 1. 입력은 공백 단위로 받으므로 80자씩 끊어준다.
# 2. 태그가 들어있으면 태그 명령대로 실행하면 된다.
sentence = []

while word_storage :
    word = word_storage.popleft()

    if word == "" :
        continue

    if word in ["<br>","<hr>"] :
        sentence = tag_cmd(word,sentence)
        continue
    
    #tag 없고 공백 아닐 때 sentence에 넣어주고 길이 체크만 진행한다.
    sentence.append(word)

    if len(" ".join(sentence)) >= 80 :
        popped_word = sentence.pop()
        word_storage.appendleft(popped_word)

        print(" ".join(sentence))

        sentence = []
        continue

print(" ".join(sentence))
    

