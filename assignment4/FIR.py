import numpy as np

def convolve(x, h):
    y_size = len(x) + len(h) - 1
    y = []
    for i in range(y_size):
        y.append(0)
        for j in range(len(h)):
            if i - j >= 0 and i - j < len(x):
                y[i] += x[i - j] * h[j]
    
    return y  # Return both the result and the zero position

def difference_equation(B, x):
    # Get length of M and N
    M = len(B) - 1

    # Instantiate y_out for use in summations
    y_out = np.array([])

    # Calculate values for summation of input and add to y_out
    for n in range(M + 1):
        y_n = sum(B[r] * (x[n - r] if n - r >= 0 else 0) for r in range(M + 1))
        y_out = np.append(y_out, y_n) 

    return y_out

def IDFT(X):
    N = len(X)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(2j * np.pi * n * k / N)
    x = np.dot(W, X) / N
    return x.real  # Return the real part of the inverse DFT