#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

static vector<pair<int, int>> spots;

int dis(pair<int, int> a, pair<int, int> b) {
    int x = a.first - b.first;
    int y = a.second - b.second;
    return x * x + y * y;  // 제곱 거리 계산
}

int min(int a, int b, int c) {
    return std::min(a, std::min(b, c));
}

int closest(int start, int end) {
    int size = end - start + 1;
    if (size == 2) return dis(spots[start], spots[start + 1]);
    else if (size == 3) {
        return min(dis(spots[start], spots[start + 1]), dis(spots[start], spots[start + 2]), dis(spots[start + 1], spots[start + 2]));
    }

    int mid = (start + end) / 2;
    int MIN = min(closest(start, mid), closest(mid + 1, end));

    vector<pair<int, int>> vec;
    int line = (spots[mid].first + spots[mid + 1].first) / 2;

    for (int i = start; i <= end; i++) {  // 범위 수정
        if (abs(line - spots[i].first) < MIN) {
            vec.push_back(spots[i]);
        }
    }

    sort(vec.begin(), vec.end(), [](pair<int, int> a, pair<int, int> b) {
        return a.second < b.second;
    });

    for (int i = 0; i < vec.size(); i++) {
        for (int j = i + 1; j < vec.size(); j++) {
            int temp = vec[j].second - vec[i].second;
            int temp2=vec[j].first-vec[i].first;
            if (temp*temp >= MIN) break;
            else if(temp2*temp2>=MIN) continue;
            else MIN = min(MIN, dis(vec[i], vec[j]));
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
        return a.first < b.first;
    });

    cout <<closest(0, n - 1) << endl;
}