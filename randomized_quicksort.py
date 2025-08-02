import random

def randomized_quicksort(arr):
    """
    Implements the Randomized Quicksort algorithm to sort a list.

    Args:
        arr: The list of elements to be sorted.

    Returns:
        A new list containing the sorted elements.
    """
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Choose a random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)

if __name__ == "__main__":
    arr = [5, 3, 8, 4, 2, 7, 1, 10]
    sorted_arr = randomized_quicksort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)
