#include<iostream>
#include<algorithm>
using namespace std;

struct A {
	int x;
	int y;
};
int main() {
	int n,rank=1;
	cin >> n;
	A* arr = new A[n];
	for (int i = 0; i < n; i++) {
		cin >> arr[i].x >> arr[i].y;
	}
	for (int i = 0; i < n; i++) {
		rank = 1;
		for (int j = 0; j < n; j++) {
			if (arr[i].x < arr[j].x && arr[i].y < arr[j].y) {
				rank++;
			}
		}
		cout << rank<<' ';
	}
}