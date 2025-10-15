#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int main(){
	fastio;
	int x,n,t1,t2;
	cin>>x;
	cin>>n;
	int sum=0;
	for(int i=0;i<n;i++){
		cin>>t1>>t2;
		sum+=t1*t2;
	}
	if(x==sum) cout<<"Yes";
	else cout<<"No";
}