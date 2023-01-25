from collections import deque

def findDist(startloc, end): #시작위치와 숫자을 주고 거리를 return 함
    curr, curc = startloc # 현재 위치
    curLoc = ((curr,curc,0))
    queue = deque()
    queue.append(curLoc)
    while queue:
        curr, curc, dist = queue.popleft()
        if keypad[curr][curc] == end:
            return ((curr,curc,dist))
        for i in range(4):
            nr, nc = curr + dr[i], curc + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 3:
                curLoc = ((nr, nc, dist + 1))
                queue.append(curLoc)

def solution(numbers, hand):
    answer = ''
    global keypad, dr, dc

    dr, dc = (1,-1,0,0), (0,0, -1,1)

    keypad = [[0] * 3 for _ in range(4)] #키패드 생성
    for r in range(3):
        for c in range(3):
            keypad[r][c] = 3 * r + c + 1
    keypad[3][0] = -1 # 별을 의미
    keypad[3][1] = 0
    keypad[3][2] = -2 # #을 의미
    leftloc, rightloc = (3,0), (3,2)
    answer = []
    for number in numbers: #숫자에 따라서 행동을 개시
        if number == 1 or number == 4 or number == 7:
            leftr,leftc,leftdist = findDist(leftloc, number)
            leftloc = leftr, leftc
            answer.append('L')
        elif number == 3 or number == 6 or number == 9:
            rightr, rightc, rightdist = findDist(rightloc, number)
            rightloc = rightr, rightc
            answer.append('R')
             # 오른쪽 시작점에서 시작하여 숫자와의 거리 구함
        else:
            leftr, leftc, leftdist = findDist(leftloc, number)
            rightr, rightc, rightdist = findDist(rightloc, number)
            if leftdist > rightdist: #만약 왼쪽에서 출발하는게 dist가 더 크다면
                answer.append('R')
                rightloc = rightr, rightc
            elif rightdist > leftdist:
                leftloc = leftr, leftc
                answer.append('L')
            else:#만약에 같다면
                if hand == "left":
                    leftloc = leftr, leftc
                    answer.append('L')
                else:
                    answer.append('R')
                    rightloc = rightr, rightc        
    answer = ''.join(answer)

    return answer