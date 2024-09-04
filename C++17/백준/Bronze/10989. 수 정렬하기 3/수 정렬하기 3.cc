#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, input[10001] = { 0 };;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        input[temp] += 1;
    }
    for (int i = 1; i < 10001; i++) {
        for (int j = 0; j < input[i]; j++) {
            cout << i << '\n';
        }
    }
}