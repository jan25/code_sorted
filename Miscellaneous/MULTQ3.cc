/*
  DATE 07 07 2015
  segment tree + lazy propogation
*/

#include <bits/stdc++.h>
using namespace std;
#define mid (l+r)/2
#define m2 (i<<1)
const int N = 1e5;
int st[4*N][3];
int lazy[4*N];
#define gc getchar_unlocked
#define pc putchar_unlocked
#define isd(c) (c >= '0' && c <= '9')

int n, q;

inline void pi(int x) {
	printf("%d\n", x);
}

inline int gi() {
	int x; scanf("%d", &x); return x;
}

void rotate(int ar[], int x) {
	if (!x) return ;
	if (x == 1) {
		swap(ar[0], ar[2]);
		swap(ar[1], ar[2]);
		return ;
	}
	if (x == 2) {
		swap(ar[1], ar[0]);
		swap(ar[1], ar[2]);
		return ;
	}
}

void sh_rot(int i, int x) {
	lazy[i] += x;
	rotate(st[i], x%3);
}

void pass(int i, int l, int r) {
	if (!lazy[i] || r == l) return;
	sh_rot(m2 + 1, lazy[i]);
	sh_rot(m2 + 2, lazy[i]);
	lazy[i] = 0;
}

void _inc(int x, int y, int i = 0, int l = 0, int r = n - 1) {
	if (x > r || y < l) return ;
	if (x <= l && y >= r) {
		sh_rot(i, 1);
		return ;
	}
	pass(i, l, r);
	_inc(x, y, m2 + 1, l, mid);
	_inc(x, y, m2 + 2, mid + 1, r);
	for (int j = 0; j < 3; ++j)
		st[i][j] = st[m2 + 1][j] + st[m2 + 2][j];
}

int _count(int x, int y, int i = 0, int l = 0, int r = n - 1) {
	if (x > r || y < l) return 0;
	if (x <= l && y >= r) return st[i][0];
	pass(i, l, r);
	return _count(x, y, m2 + 1, l, mid) +
			_count(x, y, m2 + 2, mid + 1, r);
}

void build(int i = 0, int l = 0, int r = n - 1) {
	if (r == l) {
		st[i][0] = 1;
		return ;
	}
	build(m2 + 1, l, mid);
	build(m2 + 2, mid+1, r);
	st[i][0] = r - l + 1;
}

inline void solve() {
	build();
	int o, a, b;
	while (q--) {
		o = gi(); a = gi(); b = gi();
		if (o) {
			pi(_count(a, b));
		} else {
			_inc(a, b);
		}
	}
}

int main() {	
	n = gi(); q = gi();
	solve();

	return 0;
}
