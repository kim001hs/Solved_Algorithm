#include<iostream>
using namespace std;

int main() {
	int a, b, c;
	cin >> a>> b>> c;
	int n = 10;
	int temp = b / 10;
	while(temp!=0) {
		temp /= 10;
		n *= 10;
	}
	cout << a + b - c << "\n" << n * a + b - c;
}