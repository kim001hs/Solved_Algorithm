#include <iostream>
#include <map>
using namespace std;

int main(void)
{
	map<string, bool> map;
	int n,m;
	string str;
	int res = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++)
	{
		cin >> str;
		map.insert(pair<string, bool>(str, true));
	}

	for (int i = 0; i < m; i++)
	{
		cin >> str;
		if (map[str] == true)
			res++;
	}
	cout << res;
}