#include<iostream>
#include<algorithm>
using namespace std;
struct A{
    int x;
    int y;
};
bool compare(A a,A b){
    if(a.y==b.y){
        return a.x<b.x;
    }
    return a.y<b.y;
}
int main(){
    int n;
    cin>>n;
    A* arr=new A[n];
    for(int i=0;i<n;i++){
        cin>>arr[i].x>>arr[i].y;
    }
    sort(arr,arr+n,compare);
    for(int i=0;i<n;i++){
        cout<<arr[i].x<<' '<<arr[i].y<<"\n";
    }
}