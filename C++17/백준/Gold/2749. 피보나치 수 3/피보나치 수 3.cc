#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
//1500000 피사노주기
int main(){
	fastio;
	long long n;
	cin>>n;
	n%=1500000;
	int a=0,b=1,temp=0;
	n--;
	if(n==0) temp=1;
	while(n>0){
		temp=a+b;
		temp%=1000000;
		a=b;
		b=temp;
		n--;
	}
	cout<<temp;
}