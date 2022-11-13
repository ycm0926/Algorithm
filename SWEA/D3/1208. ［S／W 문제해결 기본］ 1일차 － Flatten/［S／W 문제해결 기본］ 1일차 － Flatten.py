for i in range(1,11):
    dump = int(input())
    box = list(map(int, input().split()))
    while dump > 0:
        dump -= 1
        box[box.index(max(box))]-=1
        box[box.index(min(box))]+=1

    res = max(box) - min(box)
    print(f'#{i} {res}')