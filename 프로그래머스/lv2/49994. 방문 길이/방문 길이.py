def solution(dirs):
    answer = 0
    x, y = 5, 5
    check = []
    move_dic = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}   
    
    for i in dirs:
        dx, dy = move_dic[i]
        
        if x+dx < 0 or x+dx > 10 or y+dy < 0 or y+dy > 10:
            continue
        
        check.append((x,y,x+dx,y+dy))
        check.append((x+dx,y+dy,x,y))
        
        x = x + dx
        y = y + dy
        
    answer = len(set(check))//2
    return answer