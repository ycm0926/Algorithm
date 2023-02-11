def solution(s):
    st = list()
    for c in s:
        if c == '(':            # '(' 는 추가
            st.append(c)

        if c == ')':            # ')' 라면 바로 pop
            try:                # IndexError 발생 시 바로 False
                st.pop()        
            except IndexError:
                return False

    return len(st) == 0         # 비었다면 True 
