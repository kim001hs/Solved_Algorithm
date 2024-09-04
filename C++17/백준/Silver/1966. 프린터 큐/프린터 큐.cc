#include<iostream>
#include<queue>
using namespace std;

int main() {
	int n,N, M,input,count;
	cin >> n;
	for (int i = 0; i < n; i++) {
		count = 0;
		queue < pair<int, int>> q;
		priority_queue<int> pq;
		cin >> N >> M;
		for (int j = 0; j < N; j++) {
			cin >> input;
			q.push({ j,input });
			pq.push(input);
		}
		while (!q.empty()) {
			int order = q.front().first;
			int value = q.front().second;
			q.pop();
			if (pq.top() == value) {
				pq.pop();
				++count; 
				if (order == M) {
					cout << count << "\n";
				}
			}
			else {
				q.push({ order,value });
			}
		}
	}
}