#include <bits/stdc++.h>
#define fastio ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)
using namespace std;
int main(){
	fastio;
	int n, m; cin >> n >> m;

    set<pair<int, int>> n_set, m_set;
    vector <int> rec(n + m + 1);
    for (int i(1); i <= n + m; i++)
    {
        int x; cin >> x;
        rec[i] = x;
        (i > n ? m_set : n_set).insert({ x, i });
    }
 
    int q; cin >> q;
    while (q--)
    {
        char c; cin >> c;
        if (c == 'U')
        {
            int x, y; cin >> x >> y;
            auto& S(x > n ? m_set : n_set);
 
            S.erase({ rec[x], x });
            S.insert({ rec[x] = y, x });
        }
        else
            cout << (*n_set.begin()).second << ' ' << (*m_set.begin()).second << '\n';
    }
}