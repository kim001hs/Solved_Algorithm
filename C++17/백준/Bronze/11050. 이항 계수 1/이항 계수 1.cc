#include<iostream>
using namespace std;

int main() {
	int n, k, res = 1;
	cin >> n >> k;
	for (int i = 0; i < k; i++) {
		res *= (n - i);
	}
	for (int i = 0; i < k; i++) {
		res /= (k - i);
	}
	cout << res;
}