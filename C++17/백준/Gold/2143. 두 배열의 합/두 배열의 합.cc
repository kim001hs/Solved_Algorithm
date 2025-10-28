#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
int main(){
	fastio;
	int t, n, m;
	cin>>t;

	cin>>n;
	vector<int> arr1(n + 1, 0);
	arr1[0]=0;
	for(int i=1; i<=n; i++) {
		cin>>arr1[i];
		arr1[i]+=arr1[i-1];//누적합 배열로 바꾸기
	}

	cin>>m;
	vector<int> arr2(m + 1, 0);
	arr2[0]=0;
	for(int i=1; i<=m; i++) {
		cin>>arr2[i];
		arr2[i]+=arr2[i-1];//누적합 배열로 바꾸기
	}

	unordered_map<int, int> subtotal1, subtotal2;

	for(int i=0; i<=n; i++) {
		for(int j=i+1; j<=n; j++) {
			int temp = arr1[j]-arr1[i];
			subtotal1[temp]++;//부분합의 개수 저장
		}
	}

	for(int i=0; i<=m; i++) {
		for(int j=i+1; j<=m; j++) {
			int temp = arr2[j]-arr2[i];
			subtotal2[temp]++;//부분합의 개수 저장
		}
	}

	long long count = 0;
	for (auto &p : subtotal1) {
		int val = p.first;
		count += (long long)p.second * subtotal2[t - val];
	}
	cout<<count;
}