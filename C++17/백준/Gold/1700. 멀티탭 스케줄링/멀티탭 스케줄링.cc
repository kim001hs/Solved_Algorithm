#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;
int is_in(vector<int>&, int);
int main(){
	int n,k;
	int count=0;
	cin>>n>>k;
	vector<int> vec,multitab;
	for(int j=0;j<k;j++){
		int temp;
		cin>>temp;
		vec.push_back(temp);
	}
	int i=0;
	while(multitab.size()<n && i<k){//멀티탭에 일단 꽉찰때까지 꼽기
		if (is_in(multitab, vec[i])==-1){
			multitab.push_back(vec[i]);
		}
		i++;
	}
	while(i<k){//남은 것들 중 가장 나중에 사용되는 것을 없애기}
		if (is_in(multitab,vec[i])!=-1){
			i++;
			continue;
		}
		int mulSize=multitab.size();
		int* tmp=new int[mulSize];
		int j=i;
		int l=0;
		while(l<mulSize-1 && j<k){
			int a = is_in(multitab,vec[j]);
			if (a!=-1){
				if (tmp[a]!=1){
					tmp[a]=1;
					l++;
				}
			}
			j++;
		}
		for(int j=0;j<mulSize;j++){
			if(tmp[j]!=1){
				multitab[j]=vec[i];
				count+=1;
				break;
			}
		}
		i++;
	}
	cout<<count;
}

int is_in(vector<int>& arr, int x){
	for(int i=0;i<arr.size();i++){
		if(arr[i]==x){
			return i;
		}
	}
	return -1;
}