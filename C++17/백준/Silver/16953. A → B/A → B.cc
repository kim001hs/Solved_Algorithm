#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
int main(){
	fastio;
	int a,b,count=1;
	cin>>a>>b;
	while(a<b){
		if(b%2==0){
			b/=2;
		}else if(b%10==1){
			b/=10;
		}else{
			break;
		}
		count++;
	}
	if(a==b){
		cout<<count;
	}
	else{
		cout<<-1;
	}
}