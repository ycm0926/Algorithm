roma = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
        'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

roma2 = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M',
        4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

ro1 = [input()]
ro2 = [input()]
ro = ro1+ro2

dummy = ''                                  # 임시 저장 값
total1 = 0                                  # 총 수
total2 = ''                                 # 총 아라비안 숫자

for i in ro:                                
    for j in i:
        dummy += j                          # 두 개씩 확인하기 위함
        if len(dummy) == 2:
            if dummy in roma:               # 두 개의 단어의 조합이 있다면  
                total1 += roma[dummy]
                dummy = ''
            else:                           # 두 개의 조합이 없다면
                total1 += roma[dummy[0]]
                dummy = dummy[1]
    if dummy:
        total1 += roma[dummy]
        dummy = ''

print(total1)

arab = list(map(int, str(total1)))
l_arab = 10**(len(arab)-1)

for i in arab:
    if i*l_arab in roma2:                   # 1,5,10의 경우
        total2 += roma2[i*l_arab]
    else:
        while i != 0:
            if i == 9:
                i -= 9
                total2 += roma2[9*l_arab]
            elif i > 5:
                i -= 5
                total2 += roma2[5*l_arab]
            elif i == 4:
                i -= 4
                total2 += roma2[4*l_arab]
            else:
                i -= 1
                total2 += roma2[1*l_arab]
    l_arab //= 10

print(total2)