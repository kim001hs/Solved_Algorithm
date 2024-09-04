#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
	int input, n;
	cin >> input>>n;
	char temp;
	string res;
	for (int i = 0;input!=0;i++) {
		temp=input% n;
		input /= n;
		if (temp >= 0 && temp <= 9)
		{
			temp += '0';
		}
		else {
			temp += 'A' - 10;
		}
		res+=temp;
	 }
	for (int i = res.size()-1;i>=0; i--) {
		cout << res[i];
	}
}