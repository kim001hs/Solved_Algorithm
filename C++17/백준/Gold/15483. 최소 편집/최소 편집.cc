//EditDistance
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int dp[1001][1001];
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    string s,t;
    cin >> s >> t;
    for(int i=0;i<=s.size();i++){
        dp[i][0]=i;
    }
    for(int i=1;i<=t.size();i++){
        dp[0][i]=i;
    }
    for(int i=1;i<=s.size();i++){
        for(int j=1;j<=t.size();j++){
            dp[i][j]=min({(dp[i-1][j]+1),(dp[i][j-1]+1),(dp[i-1][j-1]+(s[i-1]==t[j-1]?0:1))});
        }
    }
    cout<<dp[s.size()][t.size()];   
}