#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int main(){
	fastio;
	int t,n,m;
	cin>>t;
	while(t--){
		cin>>n>>m;
		int prev=1,cur=1,count=1;
		while(prev!=0||cur!=1){
			int temp=cur;
			cur+=prev;
			cur%=m;
			prev=temp;
			count++;
		}
		cout<<n<<" "<<count<<endl;
	}
}