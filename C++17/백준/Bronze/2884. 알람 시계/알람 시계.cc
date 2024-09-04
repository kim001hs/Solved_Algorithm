#include<iostream>

using namespace std;

int main() {
	int h,m;
	cin >> h >> m;
	h += 24;
	m += 15;
	if (m < 60) { h--; }
	cout << h % 24 << ' ' << m%60 << endl;
	return 0;
}