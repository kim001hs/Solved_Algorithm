#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

static vector<pair<int, int>> spots;

int dis(pair<int, int> a, pair<int, int> b) {//거리의 제곱을 반환
    int x = a.first - b.first;
    int y = a.second - b.second;
    return x * x + y * y; 
}

int min(int a, int b, int c) {//세 수 중 최솟값 반환
    return std::min(a, std::min(b, c));
}

int closest(int start, int end) {
    int size = end - start + 1;
    if (size == 2) return dis(spots[start], spots[start + 1]);//사이즈가 2나 3일 때는 바로 거리 최소값 반환
    else if (size == 3) {
        return min(dis(spots[start], spots[start + 1]), dis(spots[start], spots[start + 2]), dis(spots[start + 1], spots[start + 2]));
    }

    int mid = (start + end) / 2;//중간 인덱스
    int MIN = min(closest(start, mid), closest(mid + 1, end));//좌우 영역에서의 최소값

    vector<pair<int, int>> vec;
    int line = (spots[mid].first + spots[mid + 1].first) / 2;//중간선을 만들어주고 중간선과 x값 차이 제곱이 MIN보다 작은 점들만 벡터에 넣어줌

    for (int i = start; i <= end; i++) {  // 범위 수정
        int temp = line - spots[i].first;
        if (temp*temp < MIN) {
            vec.push_back(spots[i]);
        }
    }

    sort(vec.begin(), vec.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.second < b.second;//y값 기준으로 정렬
    });

    for (int i = 0; i < vec.size(); i++) {
        for (int j = i + 1; j < vec.size(); j++) {
            int temp = vec[j].second - vec[i].second;
            int temp2=vec[j].first-vec[i].first;
            if (temp*temp >= MIN) break;//y값 차이 제곱이 MIN보다 크면 break
            else MIN = min(MIN, dis(vec[i], vec[j]));//아니면 최소값 갱신
        }
    }
    return MIN;
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int temp1, temp2;
        cin >> temp1 >> temp2;
        spots.push_back(make_pair(temp1, temp2));
    }

    sort(spots.begin(), spots.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.first < b.first;//x값 기준으로 정렬
    });

    cout <<closest(0, n - 1) << endl;
}