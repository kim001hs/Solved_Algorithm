#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int main(){
	fastio;
	int n,s,temp;
	cin>>n>>s;
	int *arr=new int[n+1];
	for(int i=0;i<n;i++){
		cin>>temp;
		arr[i]=temp;
	}
	int start=0,end=0,ans=100001;
	int sum=arr[0];
	while(start<=end&&end<n){
		if(sum>=s){
			ans=min(ans,end-start+1);
			sum-=arr[start];
			start++;
		}
		else{
			end++;
			sum+=arr[end];
		}
	}
	if(ans==100001)cout<<0;
	else cout<<ans;
}