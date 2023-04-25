N = int(input())

cards = list(map(int, input().split()))
cards.sort()

M = int(input())

compare_cards = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    while start<=end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return None

for i in range(M):
    if binary_search(cards, compare_cards[i], 0, N-1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')
