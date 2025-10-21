#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
int main(){
	fastio;
	int n,t,s,e;
	cin>>n;
	int *arr=new int[n];
	static bool dp[2000][2000];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	for(int i=0;i<n;i++){
		dp[i][i]=1;//한자리 수는 무조건 팰린드롬
	}
	for(int i=0;i<n-1;i++){
		if(arr[i]==arr[i+1]){
			dp[i][i+1]=1;//길이가 2일 때 계산
		}
	}
	for(int len=3;len<=n;len++){//길이가 3일때부터 증가시키면서 계산
		for(int i=0;i+len-1<n;i++){
			int j=i+len-1;
			if(arr[i]==arr[j]&&dp[i+1][j-1]){
				dp[i][j]=1;
			}
		}
	}

	cin>>t;
	while(t--){
		cin>>s>>e;
		cout<<dp[s-1][e-1]<<'\n';
	}
}