_= input()
ring = list(map(int,input().split()))
b_ring = ring[0]

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

for i in ring[1:]:
    num = gcd(b_ring,i)
    print(f'{b_ring//num}/{i//num}')