#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

void preorder(int in_start,int in_end,int post_start,int post_end, vector<int> &inorder_index, vector<int> &postorder){
	if(in_start>in_end||post_start>post_end) return;

	int root=postorder[post_end];
	int index=inorder_index[root];
	int offset=index-in_start;
	cout<<root<<' ';
	preorder(in_start,index-1,post_start,post_start+offset-1,inorder_index, postorder);//왼쪽 자식
	preorder(index+1,in_end,post_start+offset,post_end-1,inorder_index,postorder);//오른쪽 자식
}

int main(){
	fastio;
	int n;
	cin >> n;
	vector<int> inorder_index(n+1);
	for(int i = 0; i < n; i++){
		int temp;
		cin >> temp;
		inorder_index[temp] = i;
	}
	vector<int> postorder(n);
	for(int i = 0; i < n; i++){
		cin >> postorder[i];
	}
	preorder(0, n - 1, 0, n - 1, inorder_index, postorder);
	return 0;
}