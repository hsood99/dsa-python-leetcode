from analyze_complexity import analyze_complexity

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = list(range(10**6))
    target = 999999
    index = analyze_complexity(binary_search, arr, target)
    print(f"Target found at index: {index}")
