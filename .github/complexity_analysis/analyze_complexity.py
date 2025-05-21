import time
import tracemalloc

def analyze_complexity(func, *args, **kwargs):
    """
    Analyzes time and space complexity of the passed function.
    
    Parameters:
        func : function
            The function to analyze.
        *args : tuple
            Positional arguments for the function.
        **kwargs : dict
            Keyword arguments for the function.
    
    Returns:
        The return value of the function and prints time/memory usage.
    """
    # Start memory tracking
    tracemalloc.start()
    
    # Start timing
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    # Stop memory tracking
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Report
    print(f"\nFunction: {func.__name__}")
    print(f"Execution Time: {(end_time - start_time):.6f} seconds")
    print(f"Peak Memory Usage: {peak / 1024:.2f} KB")

    return result
