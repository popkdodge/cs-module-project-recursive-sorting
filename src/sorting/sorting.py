# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    while (arrA and arrB):
        if (arrA[0] <= arrB[0]):
            item = arrA.pop(0)
            merged_arr.append(item)
        else:
            item = arrB.pop(0)
            merged_arr.append(item)
    merged_arr.extend(arrA if arrA else arrB)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mid = len(arr) // 2
        left =  arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)

        while len(left)>0 and len(right)>0:
            arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, first, mid, last):
    # Your code here
    begin_sec_arr = mid + 1

    if arr[mid] <= arr[begin_sec_arr]: #Compares the end of the first 
        #arry to the begging of the second array
        return None
    
    while first <= mid and begin_sec_arr <= last:
        if arr[first] <= arr[begin_sec_arr]:
            begin_sec_arr += 1

        else:
            value = arr[begin_sec_arr]
            index = begin_sec_arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
