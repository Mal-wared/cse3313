#include <stdio.h>

// should be output 1000

double calculate_current_y(double A[], int N, double B[], int M, double x[], double y[])
{
    double y_n = 0.0;

    // Sum of B coefficients and corresponding x values
    for (int r = 0; r <= M; r++)
    {
        y_n += B[r] * x[r];
    }

    // Sum of A coefficients (excluding a0) and corresponding y values since it doesnt need the y0 value
    for (int k = 1; k <= N; k++)
    {
        y_n -= A[k] * y[k];
    }

    return y_n;
}

int main()
{
    // Test arrays values given in the question
    double A[] = {1.0000, -2.9754, 3.8060, -2.5453, 0.8811, -0.1254};
    double B[] = {0.0013, 0.0064, 0.0128, 0.0128, 0.0064, 0.0013};
    double x[] = {0.0855, 0.2625, 0.8010, 0.0292, 0.9289, 0.7303};
    double y[] = {0.0000, 0.5785, 0.2373, 0.4588, 0.9631, 0.5468};

    int N = sizeof(A) / sizeof(A[0]) - 1;
    int M = sizeof(B) / sizeof(B[0]) - 1;

    // Calculate the current value of y[n]
    double result = calculate_current_y(A, N, B, M, x, y);

    // Open file in write mode to write the result
    FILE *file = fopen("answer.txt", "w");
    if (file == NULL)
    {
        printf("Error opening file!\n"); // error incase file does not open
        return 1;
    }

    // Write result to file
    fprintf(file, "The current value of y[n] is: %.4f\n", result);

    // Close the file
    fclose(file);

    return 0;
}