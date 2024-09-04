#include<iostream>
using namespace std;

int main() {
    int a, b, gcd, lcm;
    cin >> a >> b;

    // 유클리드 알고리즘을 사용하여 GCD 계산
    int x = a, y = b;
    while (y != 0) {
        int temp = y;
        y = x % y;
        x = temp;
    }
    gcd = x;

    // GCD와 LCM 간의 관계를 사용하여 LCM 계산
    lcm = (a * b) / gcd;

    cout << gcd << "\n" << lcm;
    return 0;
}
