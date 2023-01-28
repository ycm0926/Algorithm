import re

def solution(new_id):
    # 1단계 소문자로 치환
    new_id = new_id.lower()
    # 2단계 조건 문자 제거 re.sub(pattern, repl, string, count, flag
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    # 3단계 마침표 2번 반복되면 치환
    new_id = re.sub('[..]+','.',new_id)
    # 4단계 앞, 뒤 마침표 제거
    new_id = re.sub('^[.]|[.]$','',new_id)
    # 5단계 비었다면 a 추가
    if not new_id:
        new_id += "a"
    # 6단계 조건에 충족 시 문자들 제거
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = re.sub('[.]$','',new_id)
    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id