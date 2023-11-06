def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

array = [10, 40, 55, 60, 66 ,70,80, 98]
target_value = int(input("Enter the target number:"))
result = binary_search(array, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}")
else:
    print(f"Target {target_value} not found in the array")
