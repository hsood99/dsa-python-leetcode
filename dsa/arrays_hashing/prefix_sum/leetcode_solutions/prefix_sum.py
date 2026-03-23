
def make_prefix_array(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

def sum_range(arr, left, right):
    if left == 0:
        return arr[right]
    return arr[right] - arr[left - 1]

def make_prefix_array_opt(arr):
    prefix = (len(arr) + 1) * [0]
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix

def sum_range_opt(arr, left, right):
    return arr[right + 1] - arr[left]

arr = [5, 2, 7, 3, 6]
prefix = make_prefix_array(arr)
print(f"Prefix array of {arr}: {prefix}")
print(f"Sum between 1 to 3 of {arr} using {prefix} is {sum_range(prefix, 2, 3)}")
prefix = make_prefix_array_opt(arr)
print(f"Cleaner prefix array of {arr}: {prefix}")
print(f"Sum between 1 to 3 of {arr} using {prefix} is {sum_range_opt(prefix, 1, 3)}")