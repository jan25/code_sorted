/*
    date: 29 05 2015
*/
// segment tree. O(logN) query time.


#include <bits/stdc++.h>
using namespace std;

set<int> up;

const int N = 50000;

int n, m;
int height[N];

int s[3*N]; // segment tree


void build(int i = 1, int l = 0, int r = n - 1) {
	if (r == l) {
		s[i] = height[l];
		return;
	}
	int mid = (l + r) / 2;
	build(2*i, l, mid);
	build(2*i + 1, mid + 1, r);
	s[i] = max(s[2*i], s[2*i + 1]);
}

const int inf = INT_MAX;

int query(int x, int y, int i = 1, int l = 0, int r = n - 1) {
	if (x > r || y < l) return -inf;
	if (x <= l && y >= r) return s[i];
	int mid = (l + r) / 2;
	return max(query(x, y, 2*i, l, mid),
				query(x, y, 2*i + 1, mid + 1, r));
}

void solve() {
	build();
	int a, b;
	int ans = 0;
	for (int i = 0; i < m; ++i) {
		cin >> a >> b; --a; --b;
		b = query(a, b - 1);
		if (b <= height[a]) ++ans;
	}
	cout << ans;
}

int main() {
	ios::sync_with_stdio(0);
	cin >> n >> m;
	int prev = INT_MAX;
	int curr;
	for (int i = 0; i < n; ++i) {
		cin >> height[i];
	}
	solve();
	
	return 0;
}
