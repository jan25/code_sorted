#include <bits/stdc++.h>
#define ll long long
using namespace std;
const int N = 2*(1e6) + 7;
ll ar[N], mark[N];
ll ans[N];
ll answer = 0;
struct node {
    int left, right, qnum;
} q[N];
int sqroot;

bool comp(node a, node b) {
    if (a.left/sqroot != b.left/sqroot) {
        return a.left/sqroot < b.left/sqroot;
    }
    return a.right < b.right;
}

void add(int i) {
    answer += ar[i] + 2*mark[ar[i]]*ar[i];
    mark[ar[i]]++;
}

void remove(int i) {
    answer += (ar[i] - 2*mark[ar[i]]*ar[i]);
    mark[ar[i]]--;
}

int main() {
    ios::sync_with_stdio(0);
    int n, m; cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> ar[i];
    for (sqroot = 1; sqroot*sqroot <= n; ++sqroot);

    int a, b;
    for (int i = 0; i < m; ++i) {
        cin >> a >> b;
        q[i].left = a-1;
        q[i].right = b-1;
        q[i].qnum = i;
    }
    sort(q, q+m, comp);
    answer += ar[0];
    mark[ar[0]] = 1;
    int wl = 0, rl = 0;
    for (int i = 0; i < m; ++i) {
        int left = q[i].left;
        int right = q[i].right;
        while (wl < left) {
            remove(wl);
            wl++;
        }
        while (wl > left) {
            add(wl-1);
            wl--;
        }
        while (rl > right) {
            remove(rl);
            rl--;
        }
        while (rl < right) {
            add(rl+1);
            rl++;
        }
        ans[q[i].qnum] = answer;
    }
    for (int i = 0; i < m; ++i) {
        cout << ans[i] << "\n";
    }
    return 0;
}
