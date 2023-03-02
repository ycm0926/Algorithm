from collections import Counter

def solution(k, tangerine):
    answer = []
    cnt = 0
    tmp = Counter(tangerine).most_common()
    # tmp = sorted(Counter(tangerine).items(), key=lambda x: -x[1])
    for i in tmp:
        for _ in range(i[1]):
            answer.append(i[0])
            if len(answer) == k:
                return len(set(answer))