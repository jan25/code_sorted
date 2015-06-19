/*
	offline querying
	segment tree with point updates
	BIT sol accepted
*/

#include <bits/stdc++.h>
using namespace std;
#define sf scanf
#define pf printf

const int N = 30010;
const int Q = 200010;
int n, q;

vector<pair<int, int> > w;
vector<pair<int, int> > ktoi;
vector<pair<int, int> > atoin;
int ans[Q];

int st[3*N];

void build(int i = 0, int l = 0, int r = n - 1) {
	if (r - l < 1) {
		st[i] = 1;
		return;
	}
	int mid = (l + r)/2;
	build(2*i + 1, l, mid);
	build(2*i + 2, mid + 1, r);
	st[i] = st[2*i + 2] + st[2*i + 1];
}

void update(int x, int i = 0, int l = 0, int r = n - 1) {
	if (x > r || x < l) return ;
	if (r - l < 1) {
		st[i] = 0;
		return ;
	}
	int mid = (l + r)/2;
	if (x <= mid) update(x, 2*i + 1, l, mid);
	else update(x, 2*i + 2, mid + 1, r);
	st[i] = st[2*i + 1] + st[2*i + 2];
}

int sum(int x, int y, int i = 0, int l = 0, int r = n - 1) {
	if (x > r || y < l) return 0;
	if (x <= l && y >= r) {
		// cout << i << " " << st[i] << endl;
		return st[i];

	}
	int mid = (l + r)/2;
	return sum(x, y, 2*i + 1, l, mid) + 
			sum(x, y, 2*i + 2, mid + 1, r);
}

void print() {
	for (int i = 0; i < n; ++i) {
		cout << i << " " << sum(i, i) << " \n";
	}
	cout << endl;
}

// int bit[N + 10];

// void update(int i, int v) {
// 	while (i <= n) {
// 		bit[i] += v;
// 		i += (i & -i);
// 	}
// }

// int sum(int i) {
// 	int ans = 0;
// 	while (i > 0) {
// 		ans += bit[i];
// 		i -= i & -i;
// 	}
// 	return ans;
// }

// void build() {
// 	for (int i = 0; i < n; ++i) update(i+1, 1);
// }

void solve() {
	build();

	int k, x, y;
	int q = ktoi.size();
	int p = 0;
	int qn;
	for (int i = 0; i < q; ++i) {
		k = ktoi[i].first;
		qn = ktoi[i].second;
		x = w[qn].first;
		y = w[qn].second;
		while (p < n && atoin[p].first <= k) 
			update(atoin[p].second+1, -1), ++p;
		ans[qn] = sum(y) - sum(x-1);
	}
	for (int i = 0; i < q; ++i) {
		pf("%d\n", ans[i]);
	}
}

int main() {
	sf("%d", &n);
	int a;
	for (int i = 0; i < n; ++i) {
		sf("%d", &a);
		atoin.push_back(make_pair(a, i));
	}	
	sort(atoin.begin(), atoin.end());
	sf("%d", &q);
	int x, y, k;
	int i = 0;
	while (q--) {
		sf("%d %d %d", &x, &y, &k);
		w.push_back(pair<int, int>(x, y));
		ktoi.push_back(make_pair(k, i));
		++i;
	}
	sort(ktoi.begin(), ktoi.end());

	solve();

	return 0;
}
