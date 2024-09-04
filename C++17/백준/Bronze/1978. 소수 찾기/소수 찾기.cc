#include<iostream>

using namespace std;

int main() {
	int n, temp, sum=0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		if (temp == 2) {
			sum++;
		}
		for (int j = 2; j < temp; j++) {
			if (temp % j == 0)break;
			else if (j==temp-1) {
				sum++;
			}
		}
	}
	cout << sum;
}