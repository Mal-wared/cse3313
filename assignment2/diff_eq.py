# Test numbers
A = [1.0000, -2.9754, 3.8060, -2.5453, 0.8811, -0.1254]
B = [0.0013, 0.0064, 0.0128, 0.0128, 0.0064, 0.0013]
x = [0.0855, 0.2625, 0.8010, 0.0292, 0.9289, 0.7303]
y = [0.0000, 0.5785, 0.2373, 0.4588, 0.9631, 0.5468]

# Function that calculates the current value of y[n] for a difference equation
def difference_equation(A, B, x, y):
    # Get length of M and N
    M = len(B) - 1
    N = len(A) - 1

    # Instantiate y_out for use in summations
    y_out = 0

    # Calculate values for summation of input and add to y_out
    for r in range(M + 1):
        y_out += B[r] * x[r] 

    # Calculate values for summation of output and add to y_out
    for k in range(1, N + 1):   
        y_out -= A[k] * y[k] 

    return y_out

results = difference_equation(A, B, x, y)

# Output result
print(f"The calculated y[n] is: {results:.4f}")
    