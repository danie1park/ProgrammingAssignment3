import time
import subprocess
import os
import sys
import matplotlib.pyplot as plt

# Benchmarks the HVLCS implementation by running input files and measuring exeuction time in ms
def benchmark_test(root_dir, test_num):
    input_file = os.path.join(root_dir, 'data', f'test{test_num}.in') # Hard coded input file paths
    # Set start time
    start = time.time()
    with open(input_file, 'r') as f:
        # Runs the script
        subprocess.run([sys.executable, os.path.join(root_dir, 'src', 'main.py')], stdin=f, capture_output=True, timeout=30)
    return (time.time() - start) * 1000 # Convert to milliseconds

def main():
    # Get the root directory of the project, used for making input files easier to open in benchmark function
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    tests = list(range(1, 11))
    times = []
    
    print('Running benchmarks on 10 test cases...')
    for i in tests:
        elapsed_ms = benchmark_test(root_dir, i)
        times.append(elapsed_ms)
        print(f'test{i}: {elapsed_ms:.3f} ms')

    # Source: https://matplotlib.org/stable/tutorials/pyplot.html
    plt.figure(figsize=(8, 5))
    plt.plot(tests, times, marker='o', linestyle='-', color='blue')
    plt.title('HVLCS Runtime for 10 Test Cases')
    plt.xlabel('Test Case')
    plt.ylabel('Time (ms)')
    plt.xticks(tests)
    plt.ylim(bottom=0, top=max(times) * 1.1)
    plt.grid(True, linestyle='--', alpha=0.5)

    output_path = os.path.join(root_dir, 'data', 'benchmark_results.png')
    plt.savefig(output_path, dpi=200, bbox_inches='tight')
    print(f'Graph saved to {output_path}')

if __name__ == '__main__':
    main()
