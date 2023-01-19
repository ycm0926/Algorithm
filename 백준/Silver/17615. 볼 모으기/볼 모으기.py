import sys

N = int(input())
balls = input()
cnt = []

# 빨간공 오른쪽
cnt.append(balls.rstrip('R').count('R'))
# 파란공 오른쪽
cnt.append(balls.rstrip('B').count('B'))
# 파란공 오른쪽
cnt.append(balls.lstrip('R').count('R'))
# 파란공 오른쪽
cnt.append(balls.lstrip('B').count('B'))
print(min(cnt))

'''
TIL/회고
- 레드와 블루를 오른쪽 왼쪽으로 모으는 가능한 모든 경우인 4가지 경우를 생각한다. 
- 하나의 색상과 방향을 정해 끝 방향에 연속으로 몰려있다면 제거하고 남은 볼의 개수를 카운트한다.
- 너무 감이 안와서 답지를 보고 다시 풀었다. 
- 결국 나머지 공들은 모두 1번씩 이동하게 된다는 것을 몰라서 어려웠다..
'''