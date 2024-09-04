#include<iostream>
#include<vector>
using namespace std;

int main() {
	string temp;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		vector<int> vec;
		int res = 0;
		cin >> temp;
		for (int j = 0; j < temp.length(); j++) {
			if (temp[j] == 'O') {
				vec.push_back(1);
			}
			else {
				vec.push_back(0);
			}
			if (j != 0&&vec[j]!=0) {
				vec[j] += vec[j - 1];
			}
			res += vec[j];
		}
		cout << res<<endl;
	}
}