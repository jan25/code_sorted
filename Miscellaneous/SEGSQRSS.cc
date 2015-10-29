/*
  segment tree + lazy
  O(logn) query and update time
*/  

#include <bits/stdc++.h>
using namespace std;
#define ii pair<int, int>
#define ll long long
#define mid ((l + r)/2)
#define i2 (2 * i)
const ll maxn = 1e6 + 7;
ll ar[maxn];

ii st[4 * maxn]; // sum, sum of sq
ii lazy[4 * maxn]; // -1set 1add, x val
ll n;

void fix(ll op, ll i, ll l, ll r, ll x) {
	lazy[i].first = op;
	lazy[i].second = x;
	if (op == -1) {
		st[i].second = (r - l + 1) * x * x;
		st[i].first = (r - l + 1) * x;
	}
	else if (op == 1) {
		ll sum = st[i].first;
		ll sumq = st[i].second;
		st[i].first += (r - l + 1) * x;
		st[i].second = sumq + (r - l + 1) * x * x + 2 * x * (sum);
	}
}

void pass(ll i, ll l, ll r) {
	ll op = lazy[i].first;
	if (!op) return ;
	ll x = lazy[i].second;
	lazy[i].first = 0;
	fix(op, i2 + 1, l, mid, x);
	fix(op, i2 + 2, mid + 1, r, x);
}

ll getsum(ll i, ll x, ll y, ll l = 0, ll r = n - 1) {
	if (l > y || r < x) return 0;
	if (x <= l && y >= r) {
		return st[i].second;
	}
	pass(i, l, r);
	return getsum(i2 + 1, x, y, l, mid) +
			getsum(i2 + 2, x, y, mid + 1, r);
}

ll op; // -1set 1add
ll val;
void upd(ll i, ll x, ll y, ll l = 0, ll r = n - 1) {
	if (y < l || x > r) return ;
	if (x <= l && y >= r) {
		pass(i, l, r);
		fix(op, i, l, r, val);
		return ;
	}
	pass(i, l, r);
	upd(i2 + 1, x, y, l, mid);
	upd(i2 + 2, x, y, mid + 1, r);
	st[i].first = st[i2 + 1].first + st[i2 + 2].first;
	st[i].second = st[i2 + 1].second + st[i2 + 2].second;
}

void build(ll i = 0, ll l = 0, ll r = n - 1) {
	if (r - l < 1) {
		st[i].first = ar[l];
		st[i].second = ar[l] * ar[l];
		return ;
	}
	build(i2 + 1, l, mid);
	build(i2 + 2, mid + 1, r);
	st[i].first = st[i2 + 1].first + st[i2 + 2].first;
	st[i].second = st[i2 + 1].second + st[i2 + 2].second;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	ll t; cin >> t;
	ll tc = 1;
	while (t--) {
		memset(lazy, 0, sizeof(lazy));
		cin >> n;
		ll q; cin >> q;
		for (ll i = 0; i < n; ++i)
			cin >> ar[i];
		build();		
		cout << "Case " << tc++ << ":\n";
		while (q--) {
			ll a, b, c;
			cin >> a >> b >> c;
			--b; --c;
			op = a == 1 ? 1 : -1;
			if (a == 2) {
				// sum of sqared (b, c)
				cout << getsum(0, b, c) << endl;
			}
			else {
				cin >> val;
				upd(0, b, c);
			}
		}
	}

	return 0;
}
