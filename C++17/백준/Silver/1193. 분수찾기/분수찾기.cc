#include<iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int i=1;
	for (;n>0; i++) {
		n -= i;
	}
	n += i-1;
	if (i % 2 == 1) {
		cout << n << '/' << i - n;
	}
	else {
		cout << i - n << '/' << n;
	}
}