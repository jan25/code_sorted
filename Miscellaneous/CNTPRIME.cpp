// segment tree + lazy propagation
// sieve for prime or not

#include <bits/stdc++.h>
using namespace std;
#define sf scanf
#define pf printf

const int N = 1e6+1;
bool prime[N];

void sieve() {
	for (int i = 0; i < N; ++i) prime[i] = true;
	prime[0] = prime[1] = false;
	for (int i = 2; i*i < N; ) {
		int j = i*i;
		while (j < N) {
			prime[j] = false;
			j += i;
		}
		++i;
		while (i*i < N && !prime[i]) ++i;
	}
}

const int MAX = 1e4 + 1;
int n, q;
int p[MAX];

int st[4* MAX];
int lazy[4*MAX];

void upd(int i, int l, int r, int x) {
	if (r - l < 1) {
		st[i] = prime[x];
		return ;
	}
	lazy[i] = x;
	st[i] = (r - l + 1) * prime[x];
}

void pass(int i, int l, int r) {
	if (!lazy[i]) return ;
	int mid = (l + r)/2;
	upd(2*i + 1, l, mid, lazy[i]);
	upd(2*i + 2, mid + 1, r, lazy[i]);
	lazy[i] = 0;
}

void change(int x, int y, int v, int i = 0, int l = 0, int r = n - 1) {
	if (x > r || y < l) return ;
	if (x <= l && y >= r) {
		upd(i, l, r, v);
		return ;
	}
	pass(i, l, r);
	int mid = (l + r)/2;
	change(x, y, v, 2*i + 1, l, mid);
	change(x, y, v, 2*i + 2, mid + 1, r);
	st[i] = st[2*i + 1] + st[2*i + 2];
}

int count(int x, int y, int i = 0, int l = 0, int r = n - 1) {
	if (y < l || x > r) return 0 ;
	if (x <= l && y >= r) return st[i];
	pass(i, l, r);
	int mid = (l + r)/2;
	return count(x, y, 2*i + 1, l, mid) + 
			count(x, y, 2*i + 2, mid + 1, r);
}

void build(int i = 0, int l = 0, int r = n - 1) {
	if (r - l < 1) {
		if (prime[p[l]]) {
			st[i] = 1;
		} else st[i] = 0;
		return ;
	}
	int mid = (r + l)/2;	
	build(2*i + 1, l, mid);
	build(2*i + 2, mid + 1, r);
	st[i] = st[2*i + 1] + st[2*i + 2];
}

void solve() {
	memset(lazy, 0, sizeof(lazy));
	memset(st, 0, sizeof(st));
	build();
	int op, a, b, v;
	while (q--) {
		sf("%d %d %d", &op, &a, &b);
		--a; --b;
		if (op) {
			pf("%d\n", count(a, b));
		} else {
			sf("%d", &v);
			change(a, b, v);
		}
	}
}

int main() {
	sieve();
	int t; sf("%d", &t);
	for (int T = 1; T <= t; ++T) {
		sf("%d %d", &n, &q);
		for (int i = 0; i < n; ++i) {
			sf("%d", &p[i]);
		}
		pf("Case %d: \n", T);
		solve();
	}
		
	return 0;
}
