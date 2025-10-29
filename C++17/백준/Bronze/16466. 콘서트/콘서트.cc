#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int main(){
	fastio;
	int n;
	cin>>n;
	vector<int> v(n+1);
	v[n]=1000001;
	for(int i=0; i<n; i++){
		cin>>v[i];
	}
	sort(v.begin(), v.end());
	for(int i=0; i<=n; i++){
		if(i+1!=v[i]){
			cout<<i+1;
			break;
		}
	}
}