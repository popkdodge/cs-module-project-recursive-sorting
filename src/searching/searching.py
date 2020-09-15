# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, left, right):
    if left <= right:
        midpoint = (right + left) //2

        if arr[midpoint] == target:
            return midpoint
        elif arr[midpoint] > target:
            return binary_search(arr, target, left, midpoint - 1)
        else:
            return binary_search(arr, target, midpoint + 1, right)
    else:
        return -1

def binary_search_it(arr, target):
    
    # Your code here
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint
        
        elif arr[midpoint] > target:
            right = midpoint - 1
        
        else:
            left = midpoint + 1

    return -1  # not found
def binary_search_it_oppo(arr, target):
    
    # Your code here
    left = len(arr) - 1
    right = 0
    
    while left >= right:
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint
        
        elif arr[midpoint] < target:
            left = midpoint - 1
        
        else:
            right = midpoint + 1

    return -1 
# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def ace_dec(arr):

    if len(arr) <= 1:
        return "Array contain only one variable or it is empty!"
    else:
        if arr[0] > arr[1]:
            return "DEC"
        if arr[1] > arr[0]:
            return "ACE"

def agnostic_binary_search(arr, target):

    if ace_dec(arr) != "ACE" and ace_dec(arr) != "DEC":
        return "Array contain only one variable or it is empty!" 

    if ace_dec(arr) == "ACE":
        return binary_search_it(arr, target)
    
    if ace_dec(arr) == "DEC":
        return binary_search_it_oppo(arr,target)