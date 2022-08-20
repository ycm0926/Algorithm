a, b = map(int, input().split())

m, n = max(a, b), min(a, b)
# GCD(Greatest Common Divisor)
while n > 0:
    m, n = n, m % n

print(m)
# LCM(Least Common Multiple)
print(a*b//m)
