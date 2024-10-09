#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int D, P, Q;
    cin >> D >> P >> Q;
    int temp  =  min(P, Q);
    P = max(P, Q);
    Q = temp;
    int MIN=D+P;
    temp=D/Q+1;
    for(int i=0; i<=min(D/P,Q); i++){
        MIN = min(MIN,(Q-(D-P*i)%Q)%Q);
    }
    MIN = min(MIN,(P-(D%P))%P);
    cout<<D+MIN;
}