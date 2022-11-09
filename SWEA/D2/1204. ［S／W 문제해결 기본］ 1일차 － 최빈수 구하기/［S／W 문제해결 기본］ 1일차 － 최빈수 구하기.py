#import sys
from collections import Counter
for i in range(1, int(input())+1):
    case = int(input())
    grade = list(map(int, input().split()))
    ans = Counter(grade).most_common(1)
    print('#'+str(i)+' '+str(ans[0][0]))
