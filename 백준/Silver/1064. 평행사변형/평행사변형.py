import sys

input = sys.stdin.readline

xa, ya ,xb, yb, xc, yc = map(int,input().split())


if (xa-xb) == 0 and (xc-xb) == 0:
    print(-1.0)
elif (xa-xb) != 0 and (xc-xb) != 0 and (ya-yb)/(xa-xb) == (yc-yb)/(xc-xb): 
    print(-1.0)
else:
    a = ((((xa-xb)**2+(ya-yb)**2)**0.5)*2)+((((xa-xc)**2+(ya-yc)**2)**0.5)*2)
    b = ((((xb-xc)**2+(yb-yc)**2)**0.5)*2)+((((xb-xa)**2+(yb-ya)**2)**0.5)*2)
    c = ((((xc-xa)**2+(yc-ya)**2)**0.5)*2)+((((xc-xb)**2+(yc-yb)**2)**0.5)*2)
    print(max(a,b,c)-min(a,b,c))