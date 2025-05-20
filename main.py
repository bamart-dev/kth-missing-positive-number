

def kth_missing_positive_number(arr, k):
    """Return kth missing number from given array.

    INPUT: List of positive numbers in increating order & a positive integer k
    OUTPUT: The kth missing number
    """
    if not arr or (arr[0] == 0 and len(arr) == 1):
        return k
    if arr[0] == 1 and arr[-1] == len(arr):
        return arr[-1] + k

    arr_set = set(arr)
    missing_count = 0
    missing_number = 0

    for num in range(1, arr[-1] + k):
        if missing_count == k:
            break
        if num in arr_set:
            continue

        missing_number = num
        missing_count += 1

    return missing_number
