def longest_consective_seq(arr):
    arr.sort()
    count = 1
    maxi = 0
    for i in range(len(arr)-1):
        if arr[i] + 1 == arr[i+1]:
            count += 1
        else:
            # print(count)
            maxi = max(count,maxi) 
            count = 0
    print(maxi)
arr = list(map(int,input().split()))
longest_consective_seq(arr)
# print(ans)
