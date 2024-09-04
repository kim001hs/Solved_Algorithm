#include<iostream>

using namespace std;

int main() {
	int num,h,w,n,result;
	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> h >> w >> n;

		if (n % h == 0) {
			result = h * 100 + (n / h);
		}
		else {
			result = (n % h) * 100 + (n / h) + 1;
		}
		cout << result << endl;
	}
}