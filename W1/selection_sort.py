def selection_sort(arr_input , len_arr):
    arr = arr_input.copy()
    for i in range(len_arr):
        max_elm_indx = 0
        for j in range(len_arr - i):
            if arr[max_elm_indx] < arr[j]:
                max_elm_indx = j
        arr[max_elm_indx], arr[len_arr-1- i] = arr[len_arr -1 - i], arr[max_elm_indx]
    
    return arr

ARR = [5,4,3,1,2,4,6,8,7,-1,6,2]

print(selection_sort(ARR , len(ARR)))