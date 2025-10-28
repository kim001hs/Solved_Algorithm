#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int main(){
	fastio;
	int n, k;
	long long result = 0;
	cin>>n>>k;
	vector<pair<int, int>> jewel(n);
	vector<int> bag(k);
	for(int i=0; i<n; i++){
		cin>>jewel[i].first>>jewel[i].second;
	}
	for(int i=0; i<k; i++){
		cin>>bag[i];
	}
	sort(jewel.begin(), jewel.end());
	sort(bag.begin(), bag.end());
	priority_queue<int> pq;
	int index = 0;
	for(int i=0; i<k; i++){
		while(index < n && jewel[index].first <= bag[i]){
			pq.push(jewel[index].second);
			index++;
		}
		if(!pq.empty()){
			result += pq.top();
			pq.pop();
		}
	}
	cout<<result;
}