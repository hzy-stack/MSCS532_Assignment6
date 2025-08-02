# MSCS532_Assignment6
MSCS532 Assignment6

### Run heapsort algorithm and sorting_comparisions
In MSCS532_Assignment6 folder, run command below
```shell
# Run determintistic quick sort test
python3 quicksort.py
```

```shell
# Run randomized quick sort test
python3 randomized_quicksort.py
```

```shell
# Run sorting comparison.
python3 sorting_comparisons.py
```

Benchmark Result
```text
| Input Size | Distribution | Deterministic Time (s) | Randomized Time (s) |
| ---------- | ------------ | ---------------------- | ------------------- |
| 1000       | Random       | 0.000951               | 0.001016            |
| 1000       | Sorted       | 0.000645               | 0.001040            |
| 1000       | Reverse      | 0.000584               | 0.000979            |
| 5000       | Random       | 0.004626               | 0.004802            |
| 5000       | Sorted       | 0.003076               | 0.004614            |
| 5000       | Reverse      | 0.002820               | 0.004214            |
| 10000      | Random       | 0.007683               | 0.008850            |
| 10000      | Sorted       | 0.005463               | 0.007639            |
| 10000      | Reverse      | 0.004885               | 0.007310            |
```

### Summary of Finding
Deterministic Quicksort consistently outperformed randomized Quicksort in this empirical run, particularly on sorted and reverse-sorted inputs—an outcome that may vary depending on system-level randomness and implementation overhead.

The measured times suggest that for smaller arrays and specific pivot strategies, deterministic selection may offer a slight practical advantage. However, randomized Quicksort provides better guarantees in unpredictable or adversarial inputs, making it preferable in general-purpose libraries.
