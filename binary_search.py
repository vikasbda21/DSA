
def binary_search_iterative(arr, target):
    l, h = 0, len(arr) - 1
    while l <= h:
        mid = (l + h)//2 

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            l = mid + 1

        else:
            h = mid - 1
    
    return -1


arr = [1,3,5,7,8,11,12,15]
target = 15
tar = binary_search_iterative(arr, target)

print(tar)