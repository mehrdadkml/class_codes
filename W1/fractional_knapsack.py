arr = [(2,12),(5,8),(4,16),(2,12)]   # (weight, value)
W = 3

def fractional_knapsack(arr, W):
    density = []
    knapsack = []

    value_in_knapsack = 0

    for elm in arr:
        cost = elm[1]/elm[0]
        density.append((cost,elm))

    print(density)

    density.sort(key= lambda x: x[0], reverse=True)
    print(density)

    for elm in density:
        if elm[1][0] <= W:
            knapsack.append((elm[1] , "fraction: 1"))
            W -= elm[1][0]
            value_in_knapsack += elm[1][1]
        else:
            fraction = W/elm[1][0]
            knapsack.append((elm[1] , f"fraction: {fraction}"))
            value_in_knapsack += (elm[1][1] * fraction)
            break
    
    return knapsack, value_in_knapsack

    # for index, shalgham in enumerate(arr):
    #     print("val in first for: ", shalgham)
    #     cost = shalgham[1]/shalgham[0]
    #     density.append((index, cost))
    #     # density = [(0, 6), (1, 8/5)]

    # density.sort(key = lambda x: x[1], reverse=True)
    # print(density)

    # for elm in density:
    #     if W >=  arr[elm[0]][0]:
    #         print(arr[elm[0]][0])
    #         knapsack.append((arr[elm[0]][0] , 1))
    #         value_in_knapsack += arr[elm[0]][1]
    #         W -=  arr[elm[0]][0]

    #     else: 
    #         fraction = W/arr[elm[0]][0]
    #         knapsack.append((arr[elm[0]][0] , fraction))
    #         value_in_knapsack += ( fraction * arr[elm[0]][1])
    #         break

    # return knapsack, value_in_knapsack

print(fractional_knapsack(arr, W))



