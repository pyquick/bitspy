def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]     
    middle = [x for x in arr if x == pivot]   
    right = [x for x in arr if x > pivot]   
    return quicksort(left) + middle + quicksort(right)
def listsortex(lit:list) -> list:
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.
    
    Args:
        lit (list): A list of integers to be sorted.
        
    Returns:
        list: A new list containing the sorted integers.
    """
    n = len(lit)
    for i in lit:
        if not isinstance(i, int):
            raise ValueError("All elements in the list must be integers.")
    sorted_list = lit.copy()  # Create a copy to avoid modifying the original list
    
    #quicksort
    sorted_list = quicksort(sorted_list)
    
    return sorted_list
def show() -> None:
    lists=[1,5,733,935,25,83,80,4672,255,63,6]
    print(listsortex(lists))