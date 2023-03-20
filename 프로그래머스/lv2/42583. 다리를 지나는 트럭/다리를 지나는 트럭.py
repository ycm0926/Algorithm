from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_weight= 0
    truck_weights = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)])
    
    while bridge:
        
        answer += 1
        sum_weight -= bridge.popleft()                      # 건너간 트럭 다리에서 제거와 무게 감소

        if truck_weights:                                   # 대기 트럭이 있다면
            if sum_weight + truck_weights[0] <= weight:     # 무게 확인하여 건너갈 수 있는지 체크
                bridge.append(truck_weights.popleft())      # 건너갈 수 있다면 다리로 이동
                sum_weight += bridge[-1]                    # 총 무게 계산
            else:                                           # 무게 초과라면
                bridge.append(0)                            # 공기 추가
    return answer