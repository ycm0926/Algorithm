def solution(n):
    res = ''
    while n > 0:
        # 몫이 0보다 같거나 작아질 때 까지 나머지를 더해준다.
        n, mod = divmod(n, 3)
        res += str(mod)

    return int(res,3)