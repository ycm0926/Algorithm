import math
a, b = map(int, input().split())
res_a = 1
res_b = 1
res_c = 1
for i in range(1,a+1):
    res_a *= i
for j in range(1,b+1):
    res_b *= j

for k in range(1,a-b+1):
    res_c *= k
print(res_a//(res_b*res_c))

# a, b = map(int, input().split())
# print((math.factorial(a)//(math.factorial(b)*(math.factorial(n-k)))))