#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

struct A {
	int age;
	string name;
};
int main() {
	vector<A> list;
	int n, temp;
	string str;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp >> str;
		A a = { temp, str };
		list.push_back(a);
	}
	stable_sort(list.begin(), list.end(), [](const A& a, const A& b) {return a.age < b.age; });
	for (int i = 0; i < n; i++) {
		cout << list[i].age << ' ' << list[i].name << "\n";
	}
}