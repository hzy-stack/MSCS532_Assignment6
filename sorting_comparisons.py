import random
import time

# Deterministic Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

def generate_input(size, distribution):
    if distribution == "random":
        return [random.randint(0, size) for _ in range(size)]
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverse":
        return list(range(size, 0, -1))
    else:
        raise ValueError("Unknown distribution type")

def time_sorting(func, arr):
    start = time.time()
    func(arr)
    return time.time() - start

def run_comparison():
    sizes = [1000, 5000, 10000]
    distributions = ["random", "sorted", "reverse"]

    results = []
    for size in sizes:
        for dist in distributions:
            arr = generate_input(size, dist)
            arr_copy = arr[:]

            t_dqs = time_sorting(quicksort, arr)
            t_rqs = time_sorting(randomized_quicksort, arr_copy)

            results.append({
                "size": size,
                "distribution": dist,
                "deterministic_quicksort": t_dqs,
                "randomized_quicksort": t_rqs
            })

    print("| Input Size | Distribution   | Deterministic time (s) | Randomized time (s) |")
    print("|------------|----------------|----------------------|--------------------|")
    for r in results:
        print(f"| {r['size']:<10} | {r['distribution']:<14} | {r['deterministic_quicksort']:<20.6f} | {r['randomized_quicksort']:<18.6f} |")

if __name__ == "__main__":
    run_comparison()
