def is_partitioned(arr, len_arr, summ):
    if summ < 0:
        return False
    if len_arr == 0 and summ != 0:
        return False
    elif summ == 0:
        return True

    return is_partitioned(arr, len_arr - 1, summ) or is_partitioned(arr, len_arr-1, summ - arr[len_arr-1])


def check_prtition(arr):
    if sum(arr) % 2:
        return False

    return is_partitioned(arr, len(arr), sum(arr) // 2)


arr = [5, 2, 6, 2, 15]
print(check_prtition(arr))
