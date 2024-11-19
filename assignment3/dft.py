import numpy as np
import matplotlib.pyplot as plt
# Open the file
def get_values(file_name):
    with open(file_name, 'r') as file:
        # Read the first line
        line = file.readline().strip()

        # Split the line by commas and convert it to a list
        array = np.array(line.split(',')).astype(np.float64)

        # Print the result
        return array

def DFT(input_array):
    N = len(input_array)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * n * k / N)
    X = np.dot(W, input_array)
    return np.abs(X)
# Get input numbers and convert from string to float as well as indices
input_nums = get_values("input.csv")
indices = np.linspace(0, len(input_nums), len(input_nums))


# DFT the input numbers
dft_array = DFT(input_nums)

# Getting expected output array
expected_output_str = np.array(get_values("testout.csv"))
expected_output = expected_output_str.astype(np.float64)

# Create 2 subplots to show 2 graphs
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot DFT results on ax1 with red color
ax1.plot(indices, dft_array, 'r', label='DFT Output')
ax1.set_title("DFT Output")
ax1.set_xlim(0,1200)
ax1.set_ylim(0,2500)

# Plot correct output results on ax2 with blue color
ax2.plot(indices, expected_output, 'b', label='Correct Output')
ax2.set_title("Correct Output")
ax2.set_xlim(0,1200)
ax2.set_ylim(0,2500)

# Display w/ tight layout
plt.tight_layout()
plt.show()