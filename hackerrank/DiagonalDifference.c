#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int diagonalDifference(int a_size_rows, int a_size_cols, int** a) {
	// Complete this function
	int diagPosSlope = 0;
	int diagNegSlope = 0;
	int i;

	//printf("%d\n", *a[0]);
	for (i = 0; i < a_size_rows; i++)
	{
		diagNegSlope += (*a)[i][i];
		diagPosSlope += (*a)[i][a_size_rows - 1 - i];
}
	return (abs(diagNegSlope - diagPosSlope));
}

int main() {
	int n;
	scanf("%i", &n);
	int a[n][n];
	int a_i, a_j;
	for (a_i = 0; a_i < n; a_i++) {
		for (a_j = 0; a_j < n; a_j++) {
			scanf("%i",&a[a_i][a_j]);
		}
	}
	int result = diagonalDifference(n, n, a);
	printf("%d\n", result);
	return 0;
}
