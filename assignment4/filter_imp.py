import math
import numpy as np
import matplotlib.pyplot as plt

def get_values(file_name):
    with open(file_name, 'r') as file:
        # Read the first line
        line = file.readline().strip()

        # Split the line by commas and convert it to a list
        array = np.array(line.split(',')).astype(np.float64)

        # Print the result
        return array

def sample_signal(fs, freq1, freq2):
    x = []
    for i in range(fs):
        x.append(math.sin(2 * math.pi * freq1 * i / fs) + math.sin(2 * math.pi * freq2 * i / fs))
    return np.array(x)

def DFT(input_array):
    N = len(input_array)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * n * k / N)
    X = np.dot(W, input_array)
    return np.abs(X)

fs = 1000
sig = DFT(sample_signal(fs, 53, 370))

def graph_signal(signal):
    signal_shifted = np.fft.fftshift(signal)

    # Plot frequency domain
    plt.plot(np.linspace(-fs/2, fs/2, len(signal_shifted)), signal_shifted, 'r', label='Frequency Domain')
    plt.title("Frequency Domain")
    plt.xlabel("Frequency (Hz)")
    plt.xlim(-fs/2, fs/2)
    plt.ylabel("Magnitude")
    plt.ylim(0, 2000)
    plt.grid(True)
    
    # Add vertical lines at the input frequencies
    plt.axvline(x=53, color='g', linestyle='--', alpha=0.5)
    plt.axvline(x=370, color='g', linestyle='--', alpha=0.5)
    plt.axvline(x=-53, color='g', linestyle='--', alpha=0.5)
    plt.axvline(x=-370, color='g', linestyle='--', alpha=0.5)

    # Display w/ tight layout
    plt.tight_layout()
    plt.show()
    # DFT the input numbers

graph_signal(sig)


