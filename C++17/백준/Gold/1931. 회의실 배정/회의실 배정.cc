#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
using namespace std;
int main(){
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin>>n;
    vector<pair<int, int>> vec;
    for(int i=0; i<n; i++){
        int a, b;
        cin>>a>>b;
        vec.push_back({b, a});
    }
    sort(vec.begin(), vec.end());//종료 시점에 대해 정렬
    int idx = vec[0].first; //첫번째 종료 시점
    int cnt = 1;
    for(int i=1; i<n; i++){
        if(vec[i].second >= idx){ //시작 시점이 이전 종료 시점보다 크거나 같으면
            idx = vec[i].first; //종료 시점을 갱신
            cnt++; //카운트 증가
        }
    }
    cout<<cnt<<"\n"; //최대 회의 수 출력
    return 0;
}