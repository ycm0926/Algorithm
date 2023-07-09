import sys
import heapq


def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

input = sys.stdin.readline
t = int(input())

for i in range(t):
    min_heap = []
    max_heap = []
    nums = dict()
    k = int(sys.stdin.readline())

    for j in range(k):
        a, b = sys.stdin.readline().split()
        num = int(b)

        if a == 'I':
            # 중복 삽입일 때
            if num in nums:
                nums[num] += 1
            # 처음 삽입일 때
            else:
                nums[num] = 1
                # min_heap에 추가
                heapq.heappush(min_heap, num)
                # max_heap에 추가
                heapq.heappush(max_heap, -num)

        elif a == 'D':
            # 큐가 비어있지 않을 때만

            if not isEmpty(nums.items()):
                # 최댓값을 제거
                if num == 1:
                    # nums에 값이 없지만 max_heap에 값이 있는 경우 또는 nums에 값이 있지만 1보다 작은 경우
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del (nums[temp])
                    nums[-max_heap[0]] -= 1
                # 최솟값을 제거
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del (nums[temp])
                    nums[min_heap[0]] -= 1

    # 결과 출력
    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])