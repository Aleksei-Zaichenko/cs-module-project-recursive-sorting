# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    indexForArrA = 0
    indexForArrB = 0
    merged_arr = []

    while indexForArrA < len(arrA) and indexForArrB < len(arrB):
        if arrA[indexForArrA] <= arrB[indexForArrB]:
            merged_arr.append(arrA[indexForArrA])
            indexForArrA += 1
        else:
            merged_arr.append(arrB[indexForArrB])
            indexForArrB += 1

    merged_arr.extend(arrA[indexForArrA:])
    merged_arr.extend(arrB[indexForArrB:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) == 0 or len(arr) == 1:
        return arr

    mid = len(arr)//2

    firstlist = arr[0:mid]
    secondList = arr[mid:len(arr)]

    newList1 = merge_sort(firstlist)
    newList2 = merge_sort(secondList)

    newList = merge(newList1,newList2)

    return newList

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

