#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	int n;
	double total=0;
	cin >> n;
	double score[1001];
	for (int i = 0; i < n; i++)
	{
		cin >> score[i];
	}
	sort(score, score+n);
	for (int i = 0; i < n; i++) {
		total = total + (score[i] / score[n - 1]) * 100;
	}
	cout <<  total / n;
}