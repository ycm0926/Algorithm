def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    for i in keymap:
        for idx, k in enumerate(i):
            if k not in key_dict:
                key_dict[k] = idx+1
            elif key_dict[k] > idx+1:
                key_dict[k] = idx+1
                
    for i in targets:
        cnt = 0
        for j in i:
            if j in key_dict:
                cnt += key_dict[j]
            else:
                cnt = -1
                break
        answer.append(cnt)
        
    return answer