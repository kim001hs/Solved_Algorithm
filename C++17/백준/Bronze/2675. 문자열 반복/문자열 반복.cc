#include<iostream>

using namespace std;

int main() {
	int n, temp;
	string A;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp >> A;
		for (int j = 0; j < A.size(); j++) {
			for (int k = 0; k < temp; k++) {
				cout << A[j];
			}
		}
		cout << endl;
	}
}