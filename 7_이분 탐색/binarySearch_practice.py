n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def binarySearch_recursive(array, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] is target:
        return mid
    elif array[mid] < target:
        binarySearch_recursive(array, mid+1, end, target)
    else:
        binarySearch_recursive(array, start, mid-1, target)

def binarySearch_while(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

result_recursive = binarySearch_recursive(array, 0, len(array) - 1, target)
result_while = binarySearch_while(array, 0, len(array) - 1, target)