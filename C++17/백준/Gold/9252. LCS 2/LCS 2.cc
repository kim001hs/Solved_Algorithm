#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int main(){
	fastio;
	string a,b;
	cin>>b>>a;
	int A=a.length(), B=b.length();
	int**dp=new int*[A+1];
	for(int i=0;i<A+1;i++){
		dp[i]=new int[B+1]();
	}
	for(int i=0;i<A;i++){
		for(int j=0;j<B;j++){
			if(i==5){
				int temp=123;
			}
			if(a[i]==b[j]){
				dp[i+1][j+1]=dp[i][j]+1;
			}else{
				dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1]);
			}
		}
	}
	string res;
	int i=A,j=B;
	while(i>0 && i>0){
		if(dp[i][j]==dp[i-1][j]){
			i--;
		}
		else if(dp[i][j]==dp[i][j-1]){
			j--;
		}
		else{
			res=a[i-1]+res;
			i--,j--;
		}
	}
	cout<<dp[A][B]<<endl;
	cout<<res;
}