import matplotlib.pyplot as plt

def graph(signal, indices, xlim, ylim, title=""):
    # Plot frequency domain
    plt.plot(indices, signal, 'r', label='Frequency Domain')
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.xlim(xlim[0], xlim[1])
    plt.ylabel("Magnitude")
    plt.ylim(ylim[0], ylim[1])
    plt.grid(False)

    # Display w/ tight layout
    plt.tight_layout()
    plt.show()
    # DFT the input numbers