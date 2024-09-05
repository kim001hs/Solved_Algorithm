#include<iostream>
#include<queue>
#include<tuple>
using namespace std;
int dx[6] = { 0, 0, -1, 1, 0, 0 };
int dy[6] = { -1, 1, 0, 0, 0, 0 };
int dz[6] = { 0, 0, 0, 0, -1, 1 };//상하좌우위아래
int y, x, z, max_days = 0;
int box[100][100][100];
queue<tuple<int, int, int>> q;
void bfs();

int main() {
	cin >> x >> y >> z;
	for (int i = 0; i < z; i++) {
		for (int j = 0; j < y; j++) {
			for(int k=0; k<x; k++){
				cin >> box[i][j][k];
				if (box[i][j][k] == 1) {
					q.push(make_tuple(i, j, k));
				}
			}//입력에  1이 있으면 미리 큐에 삽입
		}
	}
	bfs();
	for (int i = 0; i < z; i++) {
		for (int j = 0; j < y; j++) {
			for (int k = 0; k < x; k++) {
				if (box[i][j][k] == 0) {
					cout << -1 << "\n";
					return 0;
				}//안익은 토마토가 있으면 -1 출력
				if (max_days < box[i][j][k])max_days = box[i][j][k];
			}//최댓값(마지막날 익은 토마토)
		}
	}
	cout << --max_days << "\n";//처음 토마토가 1이였기 때문에 1빼기
	return 0;
}

void bfs() {
	while (!q.empty()) {
		int cz = get<0>(q.front());
		int cy = get<1>(q.front());
		int cx = get<2>(q.front());
		q.pop();
		for (int i = 0; i < 6; i++) {
			int nz = cz + dz[i];
			int ny = cy + dy[i];
			int nx = cx + dx[i];
			if (nz>=0 && ny >= 0 && nx >= 0 && nz<z && ny < y && nx < x) {
				if (box[nz][ny][nx] == 0) {
					box[nz][ny][nx] = box[cz][cy][cx] + 1;//안익은 토마토면 그 자리에 몇일읹지 기록 
					q.push(make_tuple(nz, ny, nx));//큐에 삽입
				}
			}
		}
	}
}