#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
int main(){
	fastio;
	int m,n;
	cin>>m;
	cin>>n;
	bool dp[10001]={0,0};
	for (int i = 2; i <= 10000; i++) dp[i] = true; // 전부 true로 초기화
	for(int j=2;2*j<=10000;j++){
		dp[2*j]=0;
	}
	for(int i=3;i<=100;i+=2){
		if(dp[i]){
			for(int j=i*i;j<=10000;j+=i){
				dp[j]=false;
			}
		}
	}
	int sum=0;
	int min=0;
	for(int i=m;i<=n;i++){
		if(dp[i]==1){
			sum+=i;
			if(min==0){
				min=i;
			}
		}
	}

	if(sum>0){
		cout<<sum<<'\n'<<min;
	} else{
		cout<<-1;
	}
}