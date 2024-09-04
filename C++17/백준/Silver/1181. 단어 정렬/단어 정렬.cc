#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
struct A{
	int size;
	string str;
};
bool compareWith(A a, A b) {
	if (a.str.length() == b.str.length())
		return a.str < b.str;
	return a.str.length() < b.str.length();
}
int main() {
	string temp;
	int n;
	cin >> n;
	A* arr = new A[n];
	for (int i = 0; i < n; i++) {
		cin >> temp;
		arr[i].size = temp.size();
		arr[i].str = temp;
	}
	sort(arr, arr+ n, compareWith);
	for (int i = 0; i < n; i++) {
		if (i != 0) {
			if (arr[i - 1].str == arr[i].str)continue;
		}
		cout << arr[i].str<<"\n";
	}
}