#include<iostream>
#include<string>
using namespace std;

int main() 
{
	string A;
	cin >> A;
	for (int i = 0; i < A.size() / 2; i++)
	{
		if (A[i] != A[A.size() - i-1])
		{
			cout << "0";
			return 0;
		}
	}
	cout << "1";
	return 0;
}