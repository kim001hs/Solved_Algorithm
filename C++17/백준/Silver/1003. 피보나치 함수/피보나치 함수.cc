#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
long long memo[41]={0,1,};
long long fibonacci(int n){
    if (n == 0||n == 1) {
        return memo[n];
    } else if (memo[n] == 0) {
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2);
    }
    return memo[n];;
}
int main(){
    int n;
    cin>>n;
    int temp;
    for(int i=0;i<n;i++){
        cin>>temp;
        if(temp==0){
            cout<<"1 0\n";
        }else{
            fibonacci(temp);
            cout<<memo[temp-1]<<" "<<memo[temp]<<"\n";
        //1 0 1 1 2 3 5 8 13 21 34 55 89 144 (0이 나오는 횟수)
        //0 1 1 2 3 5 8 13 21 34 55 89 144 233 (1이 나오는 횟수)
        }
    }
}