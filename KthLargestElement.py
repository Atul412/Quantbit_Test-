def find_kth_largest_ele(arr,k):
    arr.sort()
    return arr[-k]
print("Enter the elements array: ");
arr = list(map(int,input().split()))
print("Enter the Kth element: ");
k = int(input())
ans = find_kth_largest_ele(arr,k)
print(ans)
