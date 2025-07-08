#include<iostream>
#include<queue>
#include<vector>
using namespace std;
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    priority_queue<int> small;
    priority_queue<int, vector<int>, greater<int>> large;
    cin >> n;
    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        if(i%2 == 0){
            small.push(a);
        } else {
            large.push(a);
        }
        if(!large.empty() && small.top() > large.top()){
            int temp = small.top();
            small.pop();
            small.push(large.top());
            large.pop();
            large.push(temp);
        }
        cout << small.top() << "\n";
    }
}