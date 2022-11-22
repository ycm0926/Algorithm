def solution(s):
    # lower로 문자열 모두 소문자로 만들어 개수 비교
    return s.lower().count("p") == s.lower().count("y")
    
'''
# 다른사람 풀이

from collections import Counter
def solution(s):
    c = Counter(s.lower())
    return c['y'] == c['p']
    
TIL/회고
- Counter 함수도 익숙해지면 좋을듯하다.
'''
