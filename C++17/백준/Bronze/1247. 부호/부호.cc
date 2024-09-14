#include<iostream>
#include<algorithm>
using namespace std;
void check(int n){
    int overflow = 0;
    long long temp,sum=0;
    for(int i=0; i<n; i++){
        cin >> temp;
        long long temp2 = sum;
        sum += temp;
        if(temp>0&&temp2 > 0 && sum < 0) overflow += 1;
        if(temp<0&&temp2 < 0 && sum > 0) overflow -= 1;
    }
    if(overflow==0){
        if(sum == 0) cout << "0\n";
        else {
            cout<<(sum>0?"+\n":"-\n");
        }
    }else{
        cout<<(overflow>0?"+\n":"-\n");
    } 
    
}
int main(){
    int three=3;
    while(three--){
    int n;
    cin >> n;
    check(n);
    }
    return 0;
}