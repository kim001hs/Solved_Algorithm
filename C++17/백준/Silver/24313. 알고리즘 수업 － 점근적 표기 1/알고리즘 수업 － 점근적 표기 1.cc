#include<iostream>

using namespace std;

int main() {
	int a1, a0;
	int c, n0;
	cin >> a1 >> a0;
	cin >> c;
	cin >> n0;
	if (a1 <= c && a1 * n0 + a0 <= c * n0)
	{
		cout << '1';
	}
	else
	{
		cout << '0';
	}
}