n, k = map(int, input().split())
yosae = [i for i in range(1, n+1)]
ans = []
idx = 0

while yosae: # 리스트 안의 값이 없을 경우 멈춤
    idx += k-1 # 
    if idx >= len(yosae): # 포인터가 총 길이를 넘어섰을 경우
        idx %= len(yosae) # 포인터를 부족한 만큼 시작지점 이동시킴
    ans.append(yosae[idx]) # 삭제되는 값을 저장
    del yosae[idx] # 실제 배열에서 삭제시켜줌

print("<"+", ".join(map(str, ans))+">", end="")