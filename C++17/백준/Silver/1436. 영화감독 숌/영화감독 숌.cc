#include<iostream>

using namespace std;

int main() {
	int n = 0, cnt = 0,a;
	cin >> n;
	for (int i = 666;; i++) {
		a = i;
		while (a > 100) {
			if (a % 1000 == 666) {
				cnt++;
				break;
			}
			a /= 10;
		}
		if (cnt == n) { 
			cout << i; 
			return 0;
		}
	}
}