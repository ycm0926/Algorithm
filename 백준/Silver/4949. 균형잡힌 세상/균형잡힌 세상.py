while 1:
    words = input()
    stack = []

    if words == '.':
        break

    for i in words:
        if i == '[' or i == '(':  # [ or ( 입력시 스택 추가
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        print('yes')
    else:
        print('no')

