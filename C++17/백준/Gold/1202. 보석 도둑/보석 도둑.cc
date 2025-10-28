#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;

int main(){
	fastio;
	int n, k;
	long long result = 0;//long long 아니면 오버플로우
	cin>>n>>k;
	vector<pair<int, int>> jewel(n);//보석 (무게, 가격)
	vector<int> bag(k);//가방
	for(int i=0; i<n; i++){
		cin>>jewel[i].first>>jewel[i].second;//무게, 가격
	}
	for(int i=0; i<k; i++){
		cin>>bag[i];
	}
	sort(jewel.begin(), jewel.end());//무게 오름차순 정렬
	sort(bag.begin(), bag.end());//가방 오름차순 정렬
	priority_queue<int> pq;
	int index = 0;
	for(int i=0; i<k; i++){
		//가방에 넣을 수 있는 보석들 우선순위 큐에 삽입
		//index 멈추고 다음 가방은 index부터 시작하는 방식으로 시간 단축
		while(index < n && jewel[index].first <= bag[i]){
			pq.push(jewel[index].second);
			index++;
		}
		//가방에 넣을 수 있는 보석이 있다면 가장 비싼 보석 선택
		//<-pq에 남은 보석은 크기가 더 큰 가방이 넣을 수 있는 보석 리스트이므로 제거하지 않음
		if(!pq.empty()){
			result += pq.top();
			pq.pop();
		}
	}
	cout<<result;
}