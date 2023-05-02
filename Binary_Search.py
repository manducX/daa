def binary_search(arr, low, high, x):
    if high < low:
        return -1

    mid = (low + high) // 2

    if arr[mid] < x:
        return binary_search(arr, mid+1, high, x)
    elif arr[mid] > x:
        return binary_search(arr, low, mid-1, x)
    else:
        return mid

arr = input("Enter Numbers: ").split()
x = input("Enter Element to search:")
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element", x, "is present at index", result)
else:
    print("Element", x, "is not present in array")
