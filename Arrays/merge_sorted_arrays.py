def merge_sorted(arr1, arr2):

    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2

    merged_arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            merged_arr.append(arr2[j])
            j += 1

    return merged_arr + arr1[i:] + arr2[j:] # need to add the last items
    

print(merge_sorted([0, 3, 4, 31], [4, 6, 30]))
