#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);

    int n;
    priority_queue<int> pq;
    cin >> n;
    for(int i=0; i<n; i++){
        int x;
        cin >> x;
        if(x==0){
            if(pq.size()){
                cout << pq.top() << '\n';
                pq.pop();
            }else{
                cout << 0 << '\n';
            }
        }else{
            pq.push(x);
        }
    }
}