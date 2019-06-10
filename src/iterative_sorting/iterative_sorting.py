#lets do this!
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for small in range(cur_index, len(arr)):
            if arr[small] <  arr[smallest_index]:
                smallest_index = small
        # TO-DO: swap
        #temporary variable stores smallest index
        temp = arr[smallest_index]
        #smallest index will become current index
        arr[smallest_index] = arr[cur_index]
        #current index becomes the temporary variable
        arr[cur_index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr