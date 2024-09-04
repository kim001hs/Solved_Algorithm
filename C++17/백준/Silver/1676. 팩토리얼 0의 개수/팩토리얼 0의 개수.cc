#include<iostream>
using namespace std;

int main() {
	int n,res;
	cin >> n;
	res = n / 5 + n / 25 + n / 125;
	cout << res;
}