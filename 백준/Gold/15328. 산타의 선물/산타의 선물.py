import sys
from decimal import Decimal

def calculate_distance(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2).sqrt()

def can_deliver_gifts(X, houses):
    total_distance = 0
    for i in range(4):
        distance = calculate_distance(houses[i][0], houses[i][1], houses[i][2], houses[i+1][0], houses[i+1][1], houses[i+1][2])
        total_distance += distance
    
    if total_distance <= X:
        return "YES"
    else:
        return "NO"

T = int(input())  # 테스트 케이스의 개수
input = sys.stdin.readline
for _ in range(T):
    X = int(input())  # 크리스마스까지 남은 시간
    houses = [[Decimal(0), Decimal(0), Decimal(0)]]  # 초기 좌표

    for i in range(4):  # 배달하는
        houses.append(list(map(Decimal, input().split())))

    result = can_deliver_gifts(X, houses)
    print(result)

