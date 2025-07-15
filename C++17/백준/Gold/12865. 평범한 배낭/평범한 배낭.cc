#include<iostream>
#include<algorithm>
#include<vector>
struct A{
    int weight;
    int value;
};
using namespace std;
int dp[100001]={0};
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int C, n;
    cin >> n >> C;
    A *arr=new A[n+1];
    for(int i=1;i<=n;i++){
        cin >> arr[i].weight >> arr[i].value;
    }
    for(int i=1;i<=n;i++){
        for(int j=C;j>=arr[i].weight;j--){
            dp[j]=max(dp[j],dp[j-arr[i].weight]+arr[i].value);
        }
    }   
    cout << dp[C];
}