def max_(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = max_(lst[1:])
        return lst[0] if lst[0] > sub_max else sub_max


# OR


def max(list):
    if len(list) == 2:
        if list[0] > list[1]:
            return list[0]
        else:
            return list[1]

    sub_max = max(list[1:])

    if list[0] > sub_max:
        return list[0]
    else:
        return sub_max


# Divide and conquer search
def binary_search(arr, target):
    if len(arr) == 1:
        if target == arr[0]:
            return True
        else:
            return False

    middle_index = len(arr) // 2

    if target == arr[middle_index]:
        return True

    if target < arr[middle_index]:
        return binary_search(arr[:middle_index], target)
    else:
        return binary_search(arr[middle_index:], target)


arr1 = [1, 2, 3, 5, 4, 2]
arr1.sort()
print("sorted:", arr1)
print(binary_search(arr1, 4))
