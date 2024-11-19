import numpy as np
import matplotlib.pyplot as plt
import filter_graphing as fg
import FIR 

# Return all values from an input file
def get_values(file_name):
    with open(file_name, 'r') as file:
        line = file.readline().strip()
        array = np.array(line.split(',')).astype(np.float64)
        return array

# Return the DFT of an input array
def DFT(input_array):
    N = len(input_array)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * n * k / N)
    X = np.dot(W, input_array)
    return np.abs(X)

def main():
    unsampled_x = get_values("input.csv")
    x = unsampled_x[0:100]
    x_ind = np.linspace(0, 0.1, len(x))

    h = get_values("filter.csv")
    h_ind = np.linspace(0, len(h), len(h))

    # Plot input signal
    #fg.graph(x, x_ind, [0, 0.1], [-6, 6], "x[n]")
    
    # Plot filter
    #fg.graph(h, h_ind, [0, 120], [-0.05, 0.25], "br = h[k]")
    
    # Perform convolution
    # Perform difference equation
    y = FIR.convolve(x, h, 0, 50)[0:100]
    y = FIR.difference_equation(x, h)
    
    y_ind = np.linspace(0, 150, len(y))
    
    # Plot result
    fg.graph(y, y_ind, [0, 200], [-1, 1], "y[n]")
    
    X = DFT(unsampled_x)
    X_ind = np.linspace(0, 1000, len(X))
    H = DFT(h)
    H_ind = np.linspace(0, 1000, len(H))
    fg.graph(X, X_ind, [0, 1000], [0, 2000], "X[k]")

if __name__ == "__main__":
    main()







