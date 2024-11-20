#include <math.h>
#include <stdio.h>
#include <stdlib.h>

// should be defined 1000 outputs

#ifndef M_PI
#define M_PI 3.14
#endif

// Function to calculate the DFT
void calculateDFT(float* xn, int len, float* Xr, float* Xi, int N)
{
    int i, k, n;

    for (k = 0; k < N; k++) {
        Xr[k] = 0;
        Xi[k] = 0;
        for (n = 0; n < len; n++) {
            Xr[k] += xn[n] * cos(2 * M_PI * k * n / N);
            Xi[k] -= xn[n] * sin(2 * M_PI * k * n / N);
        }
    }
}

// Function to calculate the magnitude of the DFT
void calculateMagnitude(float* Xr, float* Xi, float* magnitude, int N)
{
    for (int k = 0; k < N; k++) {
        magnitude[k] = sqrt(Xr[k] * Xr[k] + Xi[k] * Xi[k]);
    }
}

// Function to read the input sequence from a CSV file
int readInputSequence(const char* filename, float** sequence)
{
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Unable to open file");
        return -1;
    }

    int len = 0;
    float value;
    while (fscanf(file, "%f,", &value) != EOF) {
        (*sequence) = realloc(*sequence, (len + 1) * sizeof(float));
        (*sequence)[len++] = value;
    }

    fclose(file);
    return len;
}

// Function to write the magnitude to a CSV file
void writeOutputSequence(const char* filename, float* magnitude, int N)
{
    FILE* file = fopen(filename, "w");
    if (!file) {
        perror("Unable to open file");
        return;
    }

    for (int i = 0; i < N; i++) {
        fprintf(file, "%f,", magnitude[i]);
    }

    fclose(file);
}

// Driver Code
int main()
{
    float* sequence = NULL;
    int len = readInputSequence("input.csv", &sequence);
    if (len < 0) {
        return 1;
    }

    int N = len; // Number of points in the DFT
    float* Xr = (float*)malloc(N * sizeof(float));
    float* Xi = (float*)malloc(N * sizeof(float));
    float* magnitude = (float*)malloc(N * sizeof(float));

    calculateDFT(sequence, len, Xr, Xi, N);
    calculateMagnitude(Xr, Xi, magnitude, N);
    writeOutputSequence("output1.csv", magnitude, N);

    free(sequence);
    free(Xr);
    free(Xi);
    free(magnitude);

    return 0;
}