#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n,temp,m;
	cin >> n;
	int* arr = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	cin >> m;
	sort(arr, arr + n);
	for (int i = 0; i < m; i++) {
		cin >> temp;
		if (binary_search(arr, arr + n, temp)) {
			cout << '1'<<' ';
		}else {
			cout << '0'<<' ';
		}
	}
}