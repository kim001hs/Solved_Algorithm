#include<iostream>

using namespace std;

int main() {
	while (1) {
		int a, b, c,temp;
		cin >> a >> b >> c;
		if (a > c) {
			temp = a;
			a = c;
			c = temp;
		}
		if (b > c) {
			temp = c;
			c = b;
			b = temp;
		}
		if (a == 0 && b== 0 && c== 0) {
			return 0;
		}
		if ((a * a + b * b) == c * c) {
			cout << "right\n";
		}
		else {
			cout << "wrong\n";
		}
	}
}