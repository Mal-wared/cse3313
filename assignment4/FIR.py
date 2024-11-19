import numpy as np

def convolve(x, h, x_zero, h_zero):
    y = np.zeros(len(x) + len(h) - 1)
    y_zero = x_zero + h_zero  # Calculate the zero position in the result
    
    for i in range(len(y)):
        sum = 0
        for j in range(len(h)):
            if (i - j + h_zero) >= x_zero and (i - j + h_zero) < (len(x) + x_zero):
                sum += x[i - j + h_zero - x_zero] * h[j]
        y[i] = sum
    
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