#include<stdio.h>
int main()
{
	int A, B, a, b, c, d, e, f;
	scanf("%d", &A);
	scanf("%d", &B);

	d = B / 100; 
	e = (B - d * 100) / 10; 
	f = (B - d * 100 - e * 10); 
	printf("%d\n", A * f); 
	printf("%d\n", A * e); 
	printf("%d\n", A * d);
	printf("%d", A * B); 
}