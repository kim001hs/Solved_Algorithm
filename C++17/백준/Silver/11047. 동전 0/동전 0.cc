#include<iostream>
#include<algorithm>
#include<stack>
using namespace std;
int main(){
    int n,k,result=0;
    cin>>n>>k;
    stack<int> s;
    while(n--){
        int num;
        cin>>num;
        s.push(num);
    }
    while(k>0&&!s.empty()){
        if(k>=s.top()){
            k-=s.top();
            result++;
        }else{
            s.pop();
        }
    }
    cout<<result;
}