#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	int n, m,max=0,stop=0,input;
	vector<int> vec;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> input;
		vec.push_back(input);
	}
	sort(vec.begin(), vec.end());
	for (int i = n-1; i > 1&&!stop; i--) {
		if (vec[i] < max / 3)break;
		for (int j = i - 1; j > 0&&!stop; j--) {
			if ((vec[i] + vec[j]) < max / 3 * 2)stop = 0;
			for (int k = j - 1; k >= 0 && !stop; k--) {
				if ((vec[i] + vec[j] + vec[k]) > max && (vec[i] + vec[j] + vec[k]) <= m) {
					max = vec[i] + vec[j] + vec[k];
				}
			}
		}
	}
	cout << max;
}