#include<iostream>

using namespace std;

int main() {
	int n,sum=0;
	string A;
	cin >> n >> A;
	for (int i = 0; i < n; i++) {
		sum += A[i] - '0';
	}
	cout << sum;
}