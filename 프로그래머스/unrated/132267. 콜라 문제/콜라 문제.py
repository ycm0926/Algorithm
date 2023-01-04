def solution(a, b, n):
    cnt = 0                     # 마신 콜라 수
    while n >= a:               # 병의 개수가 새 병으로 받을 수 있을 때 까지
        n, mod = divmod(n,a)    # 새 콜라와 남은 빈병
        n *= b                  # 받는 콜라의 개수
        cnt += n                # 마신 콜라 개수
        n += mod                # 총 남은 빈병
    return cnt