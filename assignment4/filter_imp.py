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
    x = get_values("input.csv")
    
    h = get_values("filter.csv")
    for i in range(900):
        h = np.append(h, 0)

    y = FIR.convolve(x, h)

    with open("conv_output.csv", 'w') as file:
        file.write('\n'.join(map(str, y)))

    y = FIR.difference_equation(x, h)

    with open("diff_eq_output.csv", 'w') as file:
        file.write('\n'.join(map(str, y)))

    X = DFT(x)
    X = np.append(X[int(len(X)/2):len(X)], X[0:int(len(X)/2)])
    H = DFT(h)
    H = np.append(H[int(len(H)/2):len(H)], H[0:int(len(H)/2)])

    XH = [X[i] * H[i] for i in range(len(X))]

    Y = FIR.IDFT(XH)

    with open("dft_output.csv", 'w') as file:
        file.write('\n'.join(map(str, Y)))

if __name__ == "__main__":
    main()







