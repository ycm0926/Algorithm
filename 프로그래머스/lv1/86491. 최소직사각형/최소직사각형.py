def solution(sizes):
    m_w = 0
    m_h = 0
    for h, w in sizes:
        if w < h:               #  큰 값을 h에 작은 값을 w에 넣어준다.
            h, w = w, h
        m_w = max(m_w,w)        #  w 값 비교하여 저장
        m_h = max(m_h,h)        #  h 값 작은 값 비교하여 저장

    return m_w*m_h