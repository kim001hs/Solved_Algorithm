#include<iostream>

using namespace std;
bool arr[100][100];
int S = 0;
void put(int x, int y) {
	for (int i = x; i < x + 10; i++){
		for (int j = y; j < y + 10; j++) {
			if (arr[i][j] == 0) {
				arr[i][j] = 1;
				++S;
			}
		}
	}
}
int main() {
	int num;
	int x, y;
	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> x >> y;
		put(x, y);
	}
	cout << S;
}