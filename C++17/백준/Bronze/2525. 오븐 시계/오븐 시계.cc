#include<iostream>

using namespace std;

int main()
{
	int hour, minute;
	int cookingTime;
	cin >> hour >> minute>>cookingTime;
	minute += cookingTime;
	hour += minute/60;
	cout << hour%24 << " " << minute%60;
}