#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
int main(){
	fastio;
	int m,n;
	cin>>m;
	cin>>n;
	int sum_=0;
	int min_=0;
	for(int i=sqrt(m);i<sqrt(n)+1;i++){
		int temp=i*i;
		if(temp<=n&&temp>=m){
			sum_+=temp;
			if(min_==0){
				min_=temp;
			}
		}
	}
	if(sum_==0){
		cout<<-1;
	}else{
		cout<<sum_<<'\n'<<min_;
	}
}