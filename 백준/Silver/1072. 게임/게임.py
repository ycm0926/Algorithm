X, Y = map(int,input().split())

if (Y*100//X) >= 99:                        # 승률 99퍼 이상은 절대 변하지 않는다.
    print(-1)
else:
    s = 1         
    e = X

    Z = Y*100//X

    while s <= e:
        m = (s+e)//2                        # m 만큼 횟수 증가
        
        if Z >= ((Y + m) * 100 // (X + m)): # 숭률이 z보다 작거나 같다면 s값 범위 변경
            s = m + 1
        else:                               # 승률이 z보다 크다면 e값 범위 변경
            e = m - 1
    
    print(s)