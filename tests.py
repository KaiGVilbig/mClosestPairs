import random
import time
import matplotlib.pyplot as plt
from mClosestPairs import closestPairs  # Import the function from the other file

# Trace Runs (Part c)

def run_trace_tests():
    test_cases = [
        [(0, 0), (12, 30), (40, 50), (1, 2), (2, 5), (3, 4)],  # Small input
        [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(12)],  # Random input of size 12
        [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(50)],  # Random input of size 50
    ]

    for idx, points in enumerate(test_cases):
        print(f"\nRunning Trace Test Case {idx + 1} with {len(points)} points (5 closest pairs):")
        result = closestPairs(points, 5)  # Find 5 closest pairs for each test case
        for p1, p2, dist in result:
            print(f"Pair: {p1}, {p2}, Distance: {dist:.4f}")
    print()


# Asymptotic Behavior Tests (Part d)

def measure_time_for_various_input_sizes():
    input_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    times = []

    for n in input_sizes:
        points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(n)]
        start_time = time.time()
        closestPairs(points, 10)  # Measure for finding 10 closest pairs
        end_time = time.time()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)
        print(f"Input size: {n}, Time taken: {elapsed_time:.4f} seconds")

    return input_sizes, times

def plot_results(input_sizes, times):
    plt.plot(input_sizes, times, marker='o')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time Taken (s)')
    plt.title('Asymptotic Behavior of Closest Pairs Algorithm')
    plt.grid(True)
    plt.show()


# Worst-Case Running Time Analysis (Part e)
def analyze_results(input_sizes, times):
    print("\nAnalysis of the Running Time:")
    for i in range(1, len(input_sizes)):
        if times[i - 1] == 0:
            print(f"Skipping analysis for input size {input_sizes[i - 1]} because time recorded is 0.")
            continue

        growth_factor = times[i] / times[i - 1]
        input_growth = input_sizes[i] / input_sizes[i - 1]
        log_factor = input_growth * (input_sizes[i - 1].bit_length() / input_sizes[i].bit_length())

        print(f"Input size {input_sizes[i]} compared to {input_sizes[i - 1]}:")
        print(f" - Empirical time growth factor: {growth_factor:.2f}")
        print(f" - Expected growth factor (O(n log n)): {log_factor:.2f}\n")

if __name__ == "__main__":
    run_trace_tests()

    # Part d - Measure Asymptotic Behavior and Plot
    input_sizes, times = measure_time_for_various_input_sizes()
    plot_results(input_sizes, times)

    # Part e - Analyze Running Time
    analyze_results(input_sizes, times)