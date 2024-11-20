#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define M_PI 3.14159265358979323846

void read_csv(const char *filename, double **array, int *length)
{
    FILE *file = fopen(filename, "r");
    if (!file)
    {
        perror("Can't open file");
        exit(EXIT_FAILURE);
    }

    double value;
    int count = 0;
    while (fscanf(file, "%lf,", &value) != EOF)
    {
        count++;
    }

    rewind(file);

    *array = (double *)malloc(count * sizeof(double));
    *length = count;

    for (int i = 0; i < count; i++)
    {
        fscanf(file, "%lf,", &(*array)[i]);
    }

    fclose(file);
}

void convolution(const double *input, int input_len, const double *filter, int filter_len, double **output, int *output_len)
{
    *output_len = input_len + filter_len - 1;
    *output = (double *)malloc(*output_len * sizeof(double));

    for (int i = 0; i < *output_len; i++)
    {
        (*output)[i] = 0;
        for (int j = 0; j < filter_len; j++)
        {
            if (i - j >= 0 && i - j < input_len)
            {
                (*output)[i] += input[i - j] * filter[j];
            }
        }
    }
}

// calculate the current value of y[n] for the difference equation
double calculate_current_y(double A[], int N, double B[], int M, double x[], double y[])
{
    double y_n = 0.0;

    for (int r = 0; r <= M; r++)
    {
        y_n += B[r] * x[r];
    }

    for (int k = 1; k <= N; k++)
    {
        y_n -= A[k] * y[k];
    }

    return y_n;
}

// calculate the output of the difference equation
void difference_equation(double *input, int input_len, double *A, int N, double *B, int M, double **output)
{
    *output = (double *)malloc(input_len * sizeof(double));
    double *x = (double *)calloc(M + 1, sizeof(double));
    double *y = (double *)calloc(N + 1, sizeof(double));

    for (int n = 0; n < input_len; n++)
    {
        for (int i = M; i > 0; i--)
        {
            x[i] = x[i - 1];
        }
        x[0] = input[n];

        for (int i = N; i > 0; i--)
        {
            y[i] = y[i - 1];
        }
        y[0] = calculate_current_y(A, N, B, M, x, y);
        (*output)[n] = y[0];
    }

    free(x);
    free(y);
}

void calculateDFT(double *xn, int len, double *Xr, double *Xi, int N)
{
    for (int k = 0; k < N; k++)
    {
        Xr[k] = 0;
        Xi[k] = 0;
        for (int n = 0; n < len; n++)
        {
            Xr[k] += xn[n] * cos(2 * M_PI * k * n / N);
            Xi[k] -= xn[n] * sin(2 * M_PI * k * n / N);
        }
    }
}


void calculateMagnitude(double *Xr, double *Xi, double *magnitude, int N)
{
    for (int k = 0; k < N; k++)
    {
        magnitude[k] = sqrt(Xr[k] * Xr[k] + Xi[k] * Xi[k]);
    }
}

void write_csv(const char *filename, const double *array, int length)
{
    FILE *file = fopen(filename, "w");
    if (!file)
    {
        perror("Can't open file");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < length; i++)
    {
        fprintf(file, "%lf\n", array[i]);
    }

    fclose(file);
}

int main()
{
    double *input_signal, *filter_coeffs;
    int input_len, filter_len;

    read_csv("input.csv", &input_signal, &input_len);
    read_csv("filter.csv", &filter_coeffs, &filter_len);

    // Convolution
    double *output_conv;
    int output_conv_len;
    convolution(input_signal, input_len, filter_coeffs, filter_len, &output_conv, &output_conv_len);
    write_csv("output_conv.csv", output_conv, output_conv_len);

    // Difference Equation
    double A[] = {1.0000, -2.9754, 3.8060, -2.5453, 0.8811, -0.1254};
    double B[] = {0.0013, 0.0064, 0.0128, 0.0128, 0.0064, 0.0013};
    int N = sizeof(A) / sizeof(A[0]) - 1;
    int M = sizeof(B) / sizeof(B[0]) - 1;
    double *output_diff_eq;
    difference_equation(input_signal, input_len, A, N, B, M, &output_diff_eq);
    write_csv("output_diff_eq.csv", output_diff_eq, input_len);

    // DFT
    int N_dft = input_len;
    double *Xr = (double *)malloc(N_dft * sizeof(double));
    double *Xi = (double *)malloc(N_dft * sizeof(double));
    double *magnitude = (double *)malloc(N_dft * sizeof(double));
    calculateDFT(input_signal, input_len, Xr, Xi, N_dft);
    calculateMagnitude(Xr, Xi, magnitude, N_dft);
    write_csv("output_dft.csv", magnitude, N_dft);

    free(input_signal);
    free(filter_coeffs);
    free(output_conv);
    free(output_diff_eq);
    free(Xr);
    free(Xi);
    free(magnitude);

    return 0;
}