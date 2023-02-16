
def solution(brown, yellow):
    t = brown + yellow

    for col in range(3,brown):                          # 행의 최소 개수는 3부터
        row = t//col
        if t%col == 0 and (row-2)*(col-2) == yellow:    # t에서 col의 모듈연산 나머지가 0이고 노란색 타일의 개수가 yellow 일 때
            if row > col:
                row, col = col, row
            
            return [col, row]
        
