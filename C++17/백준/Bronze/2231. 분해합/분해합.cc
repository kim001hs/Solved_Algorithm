#include<iostream>
using namespace std;

int main() {
	int input,n=0;
	cin >> input;
	int temp = input;
	for (;temp!=0; n++) {
		temp /= 10;
	}
	for (int i = 9*n;i!=0; i--) {
		temp = input - i;
		int res=0;
		while (temp > 0) {
			res += temp % 10;
			temp = temp / 10;
		}
		if (res==i) {
			cout << input - i;
			return 0;
		}
	}
	cout << '0';
	return 0;
}