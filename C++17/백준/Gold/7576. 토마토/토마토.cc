#include<iostream>
#include<queue>
using namespace std;
int dx[4] = { 0, 0, -1, 1 };
int dy[4] = { -1, 1, 0, 0 };//상하좌우
int y, x, max_days = 0;
int box[1000][1000];
queue<pair<int, int>> q;
void bfs();
int main() {
	cin >> x >> y;
	for (int i = 0; i < y; i++) {
		for (int j = 0; j < x; j++) {
			cin >> box[i][j];
			if (box[i][j] == 1) {
				q.push(make_pair(i, j));
			}
		}
	}
	bfs();
	for (int i = 0; i < y; i++) {
		for (int j = 0; j < x; j++) {
			if (box[i][j] == 0) {
				cout << -1 << "\n";
				return 0;
			}
			if (max_days < box[i][j])max_days = box[i][j];
		}
	}
	cout << --max_days << "\n";
	return 0;
}

void bfs() {
	while (!q.empty()) {
		int cy = q.front().first;
		int cx = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int ny = cy + dy[i];
			int nx = cx + dx[i];
			if (ny >= 0 && nx >= 0 && ny < y && nx < x) {
				if (box[ny][nx] == 0) {
					box[ny][nx] = box[cy][cx] + 1;
					q.push(make_pair(ny, nx));
				}
			}
		}
	}
}