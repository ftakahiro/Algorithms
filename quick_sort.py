def quick_sort(arr):
    left_arr=[]
    right_arr=[]

    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    pivot_count=0

    for i in range(len(arr)):
        if arr[i] < pivot:
            left_arr.append(arr[i])
        elif arr[i] > pivot:
            right_arr.append(arr[i])
        else:
            pivot_count+=1
    
    left_arr=quick_sort(left_arr)
    right_arr=quick_sort(right_arr)

    return left_arr+[pivot]*pivot_count+right_arr


arr = [9, 5, 8, 2, 8, 9, 7]
print(quick_sort(arr))