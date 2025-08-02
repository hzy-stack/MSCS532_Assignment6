def quicksort(arr):
    """
    Implements the Quicksort algorithm to sort a list.

    Args:
        arr: The list of elements to be sorted.

    Returns:
        A new list containing the sorted elements.
    """
    if len(arr) <= 1:
        return arr  # Base case: an array with 0 or 1 element is already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2, 7, 1, 10]
    sorted_arr = quicksort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)