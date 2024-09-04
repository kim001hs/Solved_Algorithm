#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	while (1) {
		int A[3];
		cin >> A[0]>>A[1]>>A[2];
		if (A[0] == 0)
		{
			break;
		}
		sort(A, A + 3);
		if (A[0] == 0 || (A[0] + A[1]) <= A[2]) {
			cout << "Invalid\n";
			continue;
		}
		if (A[0] == A[1] && A[1] == A[2]) {
			cout << "Equilateral\n";
		}
		else if (A[0] == A[1] || A[1] == A[2]) {
			cout << "Isosceles\n";
		}
		else {
			cout << "Scalene\n";
		}
	}
}