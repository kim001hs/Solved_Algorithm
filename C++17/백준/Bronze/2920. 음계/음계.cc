#include<iostream>
#include <algorithm>
using namespace std;

int main() {
	int input[8];
	int ascending[8] = { 1,2,3,4,5,6,7,8 };
	int descending[8] = { 8,7,6,5,4,3,2,1 };
	for (int i = 0; i < 8; i++) {
		cin >> input[i];
	}
	if (equal(input, input + 8, ascending))cout << "ascending";
	else if (equal(input, input + 8, descending))cout << "descending";
	else cout << "mixed";
}