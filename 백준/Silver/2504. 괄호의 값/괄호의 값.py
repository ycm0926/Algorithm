import sys
lst = list(input())
stack = []
res = 0
cnt = 1

for i in range(len(lst)):
    if lst[i] == '(':
        stack.append(lst[i])
        cnt *= 2
    elif lst[i] == '[':
        stack.append(lst[i])
        cnt *= 3
    elif lst[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if lst[i-1] == '(':
            res += cnt
        stack.pop()
        cnt //= 2
    elif lst[i] == ']':
        if not stack or stack[-1] == '(':
            res = 0
            break
        if lst[i-1] == '[':
            res += cnt
        stack.pop()
        cnt //= 3
if stack:
    print(0)
else:
    print(res)
'''
TIL/회고
- 문제를 차분히 이해하고 들어오는 값 순서대로 풀면 되는 문제
- ) or ] 일 때, 이전의 값이 ( or [ 인 경우에만 더해줘야 하며
- stack에 값이 있을 경우 등 예외 처리 까먹음
'''