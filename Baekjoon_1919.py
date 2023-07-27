#Baekjoon 1919 애너그램 만들기

word_dic = {}
def write_dictionary(input_word,word_dic,flag) :
    for i in input_word :
        if flag :
            if word_dic.get(i):
                word_dic[i] += 1
            else :
                word_dic[i] = 1
        else :
            if word_dic.get(i) :
                word_dic[i] -= 1
            else :
                word_dic[i] = -1
    return word_dic

write_dictionary(input(),word_dic,True)
write_dictionary(input(),word_dic,False)

result = 0
for key,value in word_dic.items() :
    result += abs(value)

print(result)