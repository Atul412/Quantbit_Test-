def Find_Missing_Nun_of_arr(arr):
    max=float("-inf")
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    # print(max)
    for i in range(len(arr)):
        if i not in arr:
            return i
arr = list(map(int,input().split()))
ans = Find_Missing_Nun_of_arr(arr)
print(ans)


    