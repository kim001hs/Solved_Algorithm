#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main() {
	vector<string> str(5);
	string temp;
	for (int i = 0; i < 5; i++)
	{
		cin >> str[i];
	}
	for (int i=0;i<15;i++)
	{
		int k = 0;
		for (int j = 0,k=0;j<5; j++) {
			if (i >= str[j].size())
			{
				++k;
			}
			else
			{
				cout << str[j][i];
			}
		}
		if (k == 5) {
			return 0;
		}
	}
}