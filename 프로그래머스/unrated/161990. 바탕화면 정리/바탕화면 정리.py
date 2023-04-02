def solution(wallpaper):
    s = [len(wallpaper),len(wallpaper[0])]
    e = [0,0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':

                # 드래그 시작점 확인
                s[0] = min(i,s[0])
                s[1] = min(j,s[1])
    
                # 드래그 끝점 확인
                e[0] = max(i+1,e[0])
                e[1] = max(j+1,e[1])
                
    return s+e