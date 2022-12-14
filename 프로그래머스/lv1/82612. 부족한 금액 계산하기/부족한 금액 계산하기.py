def solution(price, money, count):
    return (money - sum(price * i for i in range(1,count+1)))*-1 if (money - sum(price * i for i in range(1,count+1))) < 0 else 0

