#include<iostream>
using namespace std;

int main() {
	int N, r, c,res=0,n=2;
	cin >> N >> r >> c;
	while (r>=n||c>=n) {
		n *= 2;
	}
	r++;
	c++;
	n /= 2;
	while(n>=1){
		if (r - n > 0 && c - n > 0) {
			res += 3 * n * n;
			r -= n;
			c -= n;
		}
		else if (r - n > 0) {
			res += 2 * n * n;
			r -= n;
		}
		else if (c - n > 0) {
			res += n * n;
			c -= n;
		}
		n /= 2;
	}
	cout << res;
}