#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
int find(vector<int>& parent, int i) {
	if(i==-1) return -1;
    if (parent[i] == i)
        return i;
    // 경로 압축
    return parent[i] = find(parent, parent[i]);
}
int main(){
	fastio;
	int g,p,res=0;
	cin>>g;
	cin>>p;
	vector<int> parent(g);
	for(int i=0;i<g;i++) {
		parent[i]=i;
	}
	for(int i=0;i<p;i++){
		int temp;
		cin>>temp;
		int root=find(parent,temp-1);
		if(root==-1) break;
		res++;
		parent[root] = root - 1;
	}
	cout<<res;
	return 0;
}