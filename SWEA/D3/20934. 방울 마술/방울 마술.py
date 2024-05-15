T = int(input())

for test_case in range(1, T + 1):
    cups, s = input().split()
    s = int(s)
    if cups[0] == "o" and s%2 == 0:
        print(f"#{test_case} 0")
    elif cups[0] == "o" and s%2 != 0:
        print(f"#{test_case} 1")
    elif cups[1] == "o" and s%2 == 0:
        print(f"#{test_case} 1")
    elif cups[1] == "o" and s%2 != 0:
        print(f"#{test_case} 0")
    elif cups[2] == "o" and s == 0:
        print(f"#{test_case} 2")
    elif cups[2] == "o" and s%2 == 0:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} 1")
