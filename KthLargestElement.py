def find_kth_largest_ele(arr,k):
    arr.sort()
    return arr[-k]
arr = list(map(int,input().split()))
k = int(input())
ans = find_kth_largest_ele(arr,k)
print(ans)