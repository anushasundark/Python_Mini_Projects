def binary_search_string(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
sorted_strings_input = input("Enter the sorted list of strings (comma-separated): ")
sorted_strings = [s.strip() for s in sorted_strings_input.split(',')]
target_string = input("Enter the string you want to search for: ")

result = binary_search_string(sorted_strings, target_string)

if result != -1:
    print(f"String '{target_string}' found at index {result}")
else:
    print(f"String '{target_string}' not found in the list")
