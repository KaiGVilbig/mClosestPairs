import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from fpdf import FPDF
import io

# Function to analyze results and determine the type of growth
def analyze_results(input_sizes, times):
    print("\nAnalysis of the Running Time:")

    input_sizes = np.array(input_sizes)
    times = np.array(times)

    # Convert input_sizes back to Python integers for bit_length usage
    input_sizes_python = [int(size) for size in input_sizes]

    # Show empirical growth between consecutive input sizes
    growth_results = []
    for i in range(1, len(input_sizes)):
        if times[i - 1] == 0:
            growth_results.append(f"Skipping analysis for input size {input_sizes[i - 1]} because time recorded is 0.")
            continue

        growth_factor = times[i] / times[i - 1]
        input_growth = input_sizes[i] / input_sizes[i - 1]
        log_factor = input_growth * (input_sizes_python[i - 1].bit_length() / input_sizes_python[i].bit_length())

        growth_results.append(f"Input size {input_sizes[i]} compared to {input_sizes[i - 1]}:")
        growth_results.append(f" - Empirical time growth factor: {growth_factor:.2f}")
        growth_results.append(f" - Expected growth factor (O(n log n)): {log_factor:.2f}\n")

    # Plotting empirical data vs O(n log n)
    plot_image = plot_results(input_sizes, times)
    
    return growth_results, plot_image

# Plotting function
def plot_results(input_sizes, times):
    # Plot the empirical times
    plt.plot(input_sizes, times, 'bo-', label='Empirical times')

    # Create an O(n log n) line for comparison
    nlogn_times = [n * np.log(n) for n in input_sizes]
    max_time = max(times)
    scaling_factor = max_time / max(nlogn_times)  # Scaling to match the max of empirical times
    scaled_nlogn_times = [scaling_factor * t for t in nlogn_times]

    plt.plot(input_sizes, scaled_nlogn_times, 'r--', label='O(n log n)', linewidth=2)

    # Add labels and title
    plt.xlabel('Input Size')
    plt.ylabel('Running Time')
    plt.title('Empirical Running Time vs O(n log n)')
    plt.legend()

    # Save plot to a bytes buffer
    # plt.savefig(buf, format='png')
    plt.savefig('tests/plot.png', bbox_inches='tight')
    plt.close()

# Function to export analysis and plot to PDF
def export_to_pdf(growth_results, plot_image):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Running Time Analysis Report", ln=True, align='C')

    # Analysis results
    pdf.set_font("Arial", size=12)

    # Growth comparison results
    pdf.ln(10)
    pdf.cell(200, 10, txt="Empirical vs. Expected Growth:", ln=True)
    for growth in growth_results:
        pdf.multi_cell(0, 10, growth)

    # Add the plot
    pdf.ln(10)
    pdf.cell(200, 10, txt="Graph of Empirical Running Time vs O(n log n):", ln=True)
    pdf.image('tests/plot.png', x=10, y=None, w=190)

    # Save to file
    pdf.output("tests/running_time_analysis.pdf")

# Example testing script to evaluate the algorithm
def test_algorithm():
    # Sample input sizes for testing
    input_sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    
    # Record empirical times for each input size
    times = []
    for size in input_sizes:
        # Example: Call your closestPairs function and measure the time taken
        # Simulating time values for the example (you would replace this with actual time measurements)
        time_taken = np.random.rand() * size * np.log(size)
        times.append(time_taken)
    
    # Analyze and plot the results
    growth_results, plot_image = analyze_results(input_sizes, times)

    # Export the results and plot to PDF
    export_to_pdf(growth_results, plot_image)

if __name__ == "__main__":
    test_algorithm()
