#include <stdio.h>
#include <stdlib.h>
//there should be 100,000 output values

// processing arrays for the function to read and output of y array
void process_arrays(int x[], int x_size, int h[], int h_size, int y[])
{
    int y_size = x_size + h_size - 1;
    for (int i = 0; i < y_size; i++)
    {
        y[i] = 0;                        // initialize y array with 0
        for (int j = 0; j < h_size; j++) // loop through h array
        {
            // check if i - j is within the range of x array
            if (i - j >= 0 && i - j < x_size)
            {
                y[i] += x[i - j] * h[j];
            }
        }
    }
}

// calculate the output of array y
// main function to test the process_arrays function
int main()
{
    int x[] = {1, 1, 2, 3, 3, 4, 3, 2, -1};
    int h[] = {-2, -1, 3, 5, 6, 4, 2};
    int x_size = sizeof(x) / sizeof(x[0]);
    int h_size = sizeof(h) / sizeof(h[0]);

    int y_size = x_size + h_size - 1;
    int *y = malloc(y_size * sizeof(int));
    if (y == NULL)
    {
        printf("Memory allocation failed for y array\n");
        return 1;
    }

    process_arrays(x, x_size, h, h_size, y); // call the process array function

    printf("Output array of y: ");
    for (int i = 0; i < y_size; i++) // loop through y array and print the output
    {
        printf("%d ", y[i]);
    }
    printf("\n");

    // Free allocated memory
    free(y);

    return 0;
}