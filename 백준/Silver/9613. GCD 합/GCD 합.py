import sys
input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

for i in range(int(input())):
    total = 0
    nums = list(map(int,input().split()))
    l_nums = nums[0]
    nums = nums[1:]

    for j in range(l_nums-1):
        for k in range(j+1,l_nums):
            total += gcd(nums[j],nums[k])
    print(total)