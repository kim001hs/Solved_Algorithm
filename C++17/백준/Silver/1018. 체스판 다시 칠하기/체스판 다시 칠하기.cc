#include<iostream>
#include<string>
#include<vector>
using namespace std;
string A[50];
int count(int, int);
int main() {
	int n, m;
	int min= 2147483647;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> A[i];
	}
	for (int x = 0; x <= n - 8; x++)
	{
		for (int y = 0; y <= m - 8; y++)
		{
			int temp = count(x, y);
			if (temp < min)
			{
				min = temp;
			}
		}
	}
	cout << min;
}
int count(int x, int y)
{
	int bw = 0;
	int wb = 0;
	for (int i = x; i < x+8; i++)
	{
		for (int j = y; j < y+8; j++)
		{
			if ((i + j) % 2 == 1)
			{
				if (A[i][j] == 'B') {
					bw++;
				}
				else {
					wb++;
				}
			}
			else {
				if (A[i][j] == 'W') {
					bw++;
				}
				else {
					wb++;
				}
			}
		}
	}
	return ((bw < wb) ? bw : wb);
}