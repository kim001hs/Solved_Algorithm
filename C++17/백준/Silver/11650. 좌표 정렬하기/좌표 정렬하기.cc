#include<iostream>
#include<algorithm>
using namespace std;
struct xy {
	int x;
	int y;
};
bool new_sort( xy a, xy b) {
	if (a.x == b.x) { 
		return a.y < b.y; 
	}
	else {
		return a.x < b.x;
	}
}
int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	xy arr[100001];
	for (int i = 0; i < n; i++) {
		cin >> arr[i].x >> arr[i].y;
	}
	sort(arr, arr + n, new_sort);
	for (int i = 0; i < n; i++) {
		cout << arr[i].x << ' ' << arr[i].y << "\n";
	}

	return 0;
}