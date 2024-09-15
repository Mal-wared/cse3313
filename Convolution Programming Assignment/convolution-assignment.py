# Nicholas Nhat Tran 1002027150

import datetime

def convolve(x, h):
    y = 'y=['
    for i in range(len(x) + len(h) - 1):
        sum = 0
        for j in range(len(h)):
            if i - j >= 0 and i - j < len(x):
                sum += x[i - j] * h[j]
        if i < len(x) + len(h) - 2:
            y = y + str(sum) + ' '
        else:
            y = y + str(sum)
    y = y + ']'
    return y

def main():
    x = [1, 1, 2, 3, 3, 4, 3, 2, -1]
    h = [-2, -1, 3, 5, 6, 4, 2]

    # convolve y
    y = convolve(x, h)
    print(y)

    # print output of convolution to output.txt
    f = open('output.txt', 'w')
    print(y, file=f)

    # print current date and time to verify if output.txt works as expected
    now = datetime.datetime.now()
    print(now, file=f)

if __name__ == '__main__':
    main()
