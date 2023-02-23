from collections import deque

def solution(s):
    answer = 0
    
    if len(s)%2 != 0:
        return 0
    
    for i in range(len(s)-1):
        stack = [s[0]]
        
        for i in s[1:]:
            
            if not stack:
                stack.append(i)            
            elif (stack[-1] == '[' and i == ']') or (stack[-1] == '(' and i == ')') or (stack[-1] == '{' and i == '}'):
                stack.pop()
            else:
                stack.append(i)
                
        if not stack:
            answer +=1
            
        s = s[1:]+s[0]
    return answer
