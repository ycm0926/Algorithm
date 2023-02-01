def solution(babbling):
    ans = 0
    for i in babbling:
        if 'aya' in i and 'ayaaya' not in i:
            i = i.replace("aya",' ')
        if 'ye' in i and 'yeye' not in i:
            i = i.replace("ye",' ')
        if 'woo' in i and 'woowoo' not in i:
            i = i.replace("woo",' ')
        if 'ma' in i and 'mama' not in i:
            i = i.replace("ma",' ')
        if i.isspace():                         # 공백이면 카운트
            ans += 1
    return ans
