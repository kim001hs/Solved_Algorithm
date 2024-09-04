#include<iostream>
using namespace std;

int main() {
	int A, B, V,res;
	cin >> A >> B >> V;
	res = (V - A) / (A - B);
	if ((V - A) % (A - B) == 0) {
		cout << res + 1;
	}
	else {
		cout << res + 2;
	}
}