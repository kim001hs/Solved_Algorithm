#include<iostream>

using namespace std;

int main() {
	int A[9],max=0,max_num=0;
	for (int i = 0; i < 9; i++) {
		cin >> A[i];
		if (A[i] > max) {
			max = A[i];
			max_num = i+1;
		}
	}
	cout << max << endl << max_num;
}