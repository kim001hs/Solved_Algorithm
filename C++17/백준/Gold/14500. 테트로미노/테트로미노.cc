#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
void dfs(int x, int y, int d, int sum),T(int x, int y);

int N, M;
int matrix[500][500];
bool visited[500][500];
int result;

int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> matrix[i][j];
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (i == 3 && j == 0) {
				int d = 0;
			}
			dfs(i, j, 1, 0);
			T(i, j);
		}
	}
	cout << result;
}
void dfs(int y,int x, int d,int sum) {
	sum += matrix[y][x];
	visited[y][x] = true;
	if (d == 4) {
		result = (sum < result) ? result : sum;
		visited[y][x] = false;
		return;
	}
	if (x - 1 >= 0&&!visited[y][x - 1])dfs(y, x - 1, d + 1, sum);
	if (x + 1 < M && !visited[y][x + 1])dfs(y, x + 1, d + 1, sum);
	if (y - 1 >= 0 && !visited[y - 1][x])dfs(y - 1, x, d + 1, sum);
	if (y + 1 < N && !visited[y + 1][x])dfs(y + 1, x, d + 1, sum);
	visited[y][x] = false;
}
void T(int y,int x) {
	vector<int> values;
	int sum = matrix[y][x];
	if (x - 1 >= 0) values.push_back(matrix[y][x - 1]);
	if (x + 1 < M) values.push_back(matrix[y][x + 1]);
	if (y - 1 >= 0) values.push_back(matrix[y - 1][x]);
	if (y + 1 < N) values.push_back(matrix[y + 1][x]);
	if (values.size() >= 3) {
		sort(values.begin(), values.end(), greater<int>());
		sum += values[0] + values[1] + values[2];
	}
	result = (sum < result) ? result : sum;
	return;
}