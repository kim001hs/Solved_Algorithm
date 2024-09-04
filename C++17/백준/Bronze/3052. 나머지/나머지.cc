#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int arr[10];
	int temp,res=1;
	for (int i = 0; i < 10; i++) {
		cin >> temp;
		arr[i] = temp % 42;
	}
	sort(arr, arr + 10);
	for (int i = 1; i < 10; i++) {
		if (arr[i - 1] != arr[i]) {
			res++;
		}
	}
	cout << res;
}