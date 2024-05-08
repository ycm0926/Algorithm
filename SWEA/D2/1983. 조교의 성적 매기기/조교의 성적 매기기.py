
T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    students = dict()
    grade = ["D0","C-","C0","C+","B-","B0","B+","A-","A0","A+"]
    for i in range(n):
        a, b, c = map(int, input().split())
        students[i+1] = (a*0.35) + (b*0.45) + (c*0.2)
    students = sorted(students.items(), key=lambda x: x[1])

    for i,s in enumerate(students):
        if s[0] == k:
            print(f"#{test_case} {grade[(i//(n//10))]}")
            break
