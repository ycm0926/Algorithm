def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    tmp = ""
    while n > 0:
        n,r = divmod(n,k)
        tmp += str(r)
        
    tmp = tmp[::-1].split('0')
    
    for i in tmp:
        if i == "2":
            answer += 1
        elif i and i != '1':
            answer += isPrime(int(i))
    return answer

