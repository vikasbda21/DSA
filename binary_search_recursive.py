def binary_search_rec(arr, target, l, h):
    if l > h:
        return -1
    
    mid = (l + h)//2
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid+1, h)
    
    else:
        return binary_search_rec(arr, target, l, mid-1)
    



arr = [1,3,5,7,8,11,12,15]
target = 0
tar = binary_search_rec(arr, target, 0 ,  len(arr)-1)

print(tar)