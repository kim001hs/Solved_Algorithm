#include<iostream>
#include<string>
#include<queue>
#include<cstring>
using namespace std;
void bfs();
int a, b;
bool visited[10000];
int main() {
	int n;
	cin >> n;
	while(n--) {
		cin >> a >> b;
		memset(visited, false, sizeof(visited));
		bfs();
	}
}
void bfs() {
	queue<pair<int, string>> q;
	q.push(make_pair(a, ""));
	visited[a] = true;
	
	while (!q.empty()) {
		int current_num = q.front().first;
		string current_str = q.front().second;
		q.pop();

		int D, S, L, R;

		if (current_num == b) {
			cout<<current_str<<"\n";
			return;
		}

		D = 2 * current_num % 10000;
		if (!visited[D]) {
			visited[D] = true;
			q.push(make_pair(D, current_str + "D"));
		}

		S = current_num - 1 < 0 ? 9999 : current_num - 1;
		if (!visited[S]) {
			visited[S] = true;
			q.push(make_pair(S, current_str + "S"));
		}

		L = (current_num % 1000) * 10 + current_num / 1000;
		if (!visited[L]) {
			visited[L] = true;
			q.push(make_pair(L, current_str + "L"));
		}

		R = (current_num % 10) * 1000 + current_num / 10;
		if (!visited[R]) {
			visited[R] = true;
			q.push(make_pair(R, current_str + "R"));
		}
	}
}