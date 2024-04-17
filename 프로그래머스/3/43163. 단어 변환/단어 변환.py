def check(a,b):
    cnt = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt

def dfs(word,cnt,target,words,v,answer):
    
    if word == target:
        answer.append(cnt)
        return
    
    for i in range(len(words)):
        
        if v[i]: continue
        
        if check(word, words[i]) == 1:
            v[i] = True
            dfs(words[i], cnt+1, target, words,v,answer)
            v[i] = False  # 원 상태로 백트래킹
        
def solution(begin, target, words):
    answer = []
    
    if target not in words:
        return 0
    
    v = [False]*(len(words))
    
    dfs(begin,0,target,words,v,answer)
    
    return min(answer)