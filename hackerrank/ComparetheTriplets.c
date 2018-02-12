#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

/*
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and with .

If , then Alice is awarded  point.
If , then Bob is awarded  point.
If , then neither person receives a point.
Comparison points is the total points a person earned.

Given  and , can you compare the two challenges and print their respective comparison points?
 */

int* solve(int a0, int a1, int a2, int b0, int b1, int b2, int *result_size){
	// Complete this function
	int *r;

	r = malloc(sizeof(int) * 2);
	if (r == NULL)
		return (NULL);
	r[0] = 0;
	r[1] = 0;
	if (a0 > b0)
		r[0]++;
	else if (a0 < b0)
		r[1]++;
	if (a1 > b1)
		r[0]++;
	else if (a1 < b1)
		r[1]++;
	if (a2 > b2)
		r[0]++;
	else if (a2 < b2)
		r[1]++;
	*result_size = 2;
	//printf("r[0]:%d  r[1]:%d\n", r[0], r[1]);
	//printf("IN FN: result_size:%d\n", *result_size);
	return (r);
}

int main() {
	int a0;
	int a1;
	int a2;
	scanf("%d %d %d", &a0, &a1, &a2);
	//printf("ORIG: a0:%d a1:%d a2:%d\n", a0, a1, a2);
	int b0;
	int b1;
	int b2;
	scanf("%d %d %d", &b0, &b1, &b2);
	//printf("ORIG: b0:%d b1:%d b2:%d\n", b0, b1, b2);
	int result_size;
	int result_i;
	int* result = solve(a0, a1, a2, b0, b1, b2, &result_size);
	//printf("RESULT: result[0]:%d result[1]:%d\n", result[0], result[1]);
	//printf("result_size:%d\n", result_size);
	for(result_i = 0; result_i < result_size; result_i++) {
		if(result_i) {
			printf(" ");
		}
		printf("%d", result[result_i]);
	}
	puts("");

	return 0;
}
