import time

# function to benchmark a sorting algorithm
def benchmark_sort(sort_function, data, repetitions=3):
    total_time = 0 # runs the algorithm multiple times and returns average runtime

    for _ in range(repetitions):
        test_data = data.copy()
        start = time.perf_counter() # starts the timer
        sort_function(test_data) # runs the sorting algorithms
        end = time.perf_counter()  # ends the timer
        total_time += (end - start) # adds the elapsed time
    return total_time / repetitions # returns the average runtime