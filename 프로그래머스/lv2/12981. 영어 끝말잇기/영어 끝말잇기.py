
def solution(n, words):
    s_words = set([words[0]])
    num = 1
    order = 1
    for i in range(1,len(words)):
        num += 1

        if  num > n:
            num = 1
            order += 1

        if words[i] in s_words or words[i-1][-1] != words[i][0]:
            return [num,order]

        s_words.add(words[i])
    return [0,0]