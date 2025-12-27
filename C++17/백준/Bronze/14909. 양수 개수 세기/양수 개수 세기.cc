#include<iostream>
using namespace std;

int main(){
    int temp,count=0;
    while(cin>>temp){
        if(temp>0)
            count++;
    }
    cout<<count;
}