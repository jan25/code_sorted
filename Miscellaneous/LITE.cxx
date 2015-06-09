// segment tree + lazy propagation
// log(n) range query
// log(n) range update

#include <bits/stdc++.h>
using namespace std;
#define sf scanf
#define pf printf
#define iOS ios::sync_with_stdio(0)

const int N = 1e5 + 10;

int st[2 * N];

int lazy[2 * N];

void update(int i, int l, int r, int x) {
	if (!x) return ;
	if (r > l) {
		if (!lazy[i]) lazy[i] = 1;
		else lazy[i] = 0;
	}
	st[i] = (r - l + 1) - st[i];
}

void pass(int i, int l, int r) {
	int mid = (r + l) / 2;
	update(2 * i + 1, l, mid, lazy[i]);
	update(2 * i + 2, mid + 1, r, lazy[i]);
	lazy[i] = 0;
}

int n;

void on(int x, int y, int i = 0, int l = 0, int r = n - 1) {
	if (x > r || l > y) return ;
	if (x <= l && r <= y) {
		update(i, l, r, 1);
		return ;
	}
	pass(i, l, r);
	int mid = (r + l) / 2;
	on(x, y, 2*i + 1, l, mid);
	on(x, y, 2*i + 2, mid + 1, r);
	st[i] = st[2*i + 1] + st[2*i + 2];
}

int count(int x, int y, int i = 0, int l = 0, int r = n - 1) {
	
	if (x > r || y < l) return 0;
	if (x <= l && y >= r) {
		return st[i];
	}
	pass(i, l, r);
	int mid = (r + l) / 2;
	return count(x, y, 2*i + 1, l, mid) +
			count(x, y, 2*i + 2, mid + 1, r);
}

int m;

void read() {
	int op, l, r;
	while (m--) {
		sf("%d %d %d", &op, &l, &r);
		if (op) {
			pf("%d\n", count(l - 1, r - 1));
		}
		else {
			on(l, r);
		}
	}
}

int main() {
	iOS;
	memset(lazy, 0, sizeof(lazy));
	memset(st, 0, sizeof(st));
	sf("%d %d", &n, &m);
	read();
	return 0;
}
