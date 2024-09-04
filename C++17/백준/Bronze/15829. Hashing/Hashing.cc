#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main() {
	int  L, M = 1234567891;
	long long Hash=0, r = 1;
	string A;
	cin >> L>>A;
	for (int i = 0; i < L; i++) {
		Hash = (Hash + (A[i] - 96) * r) % M;
		r = r * 31 % M;
	}
	cout << Hash;
}