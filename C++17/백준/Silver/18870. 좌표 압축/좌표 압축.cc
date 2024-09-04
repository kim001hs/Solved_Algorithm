#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct stc {
	int sequence;
	int num;
	int res;
};
int main() {
	int num,temp;
	vector<stc> A;
	cin >> num;
	for (int i = 0; i < num; i++)
	{
		cin >> temp;
		stc element = { i, temp,temp };
		A.push_back(element);
	}
	sort(A.begin(), A.end(), [](const stc& a, const stc& b) {
		return a.num < b.num; });
	int j = 0; 
	A[0].res = j;
	for (int i = 1; i < num; i++) {
		if (A[i].num == A[i - 1].num) {
			A[i].res = j;
		}
		else {
			A[i].res = ++j;
		}
	}
	sort(A.begin(), A.end(), [](const stc& a, const stc& b) {
		return (a.sequence < b.sequence); });
	for (int i = 0; i < num; i++)
	{
		cout << A[i].res << ' ';
	}
	return 0;
}