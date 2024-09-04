#include<iostream>
#include<string>
using namespace std;

void FizzBuzz(int i) {
	if (i % 15 == 0) {
		cout << "FizzBuzz";
	}
	else if (i % 3 == 0) {
		cout << "Fizz";
	}
	else if (i % 5 == 0) {
		cout << "Buzz";
	}
	else {
		cout << i;
	}
}

int main() {
	string A;
	for (int i = 3; i > 0; i--) {
		cin >> A;
		try {
			int num = stoi(A);
			FizzBuzz(num + i);
			return 0;
		}
		catch (invalid_argument) {}
		catch (out_of_range) {}
	}

}