def merge(arr1, arr2):
    temp = []
    left = 0
    right = 0

    while left < len(arr1) and right < len(arr2):
        if arr1[left] <= arr2[right]:
            temp.append(arr1[left])
            left += 1

        else:
            temp.append(arr2[right])
            right += 1

    while left < len(arr1):
        temp.append(arr1[left])
        left += 1
    while right < len(arr2):
        temp.append(arr2[right])
        right += 1
    return temp


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


arr = [4, 1, 2, 4, 5]
x = merge_sort(arr)
print(x)
print(arr)
