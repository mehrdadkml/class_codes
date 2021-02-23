def bubble_sort(arr):
    res = arr.copy()
    for i in range(len(res)-1):
        print(res)
        for j in range(len(res)-i-1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    return res


print(bubble_sort([5, 8, 3, 12, -1, 4]))
