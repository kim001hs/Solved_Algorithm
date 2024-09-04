#include<iostream>
#include<string>
using namespace std;

int main() {
	string A;
	bool isPal;
	while (1) {
		isPal = 1;
		cin >> A;
		if (A == "0") {
			break;
		}
		for (int i = 0; i < (A.size() / 2); i++) {
			if (A[i] != A[A.size() - 1 - i]) {
				cout << "no"<<"\n";
				isPal = 0;
				break;
			}
		}
		if (isPal == 1) {
			cout << "yes" << "\n";
		}
	}
}