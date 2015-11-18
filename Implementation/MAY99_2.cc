// http://www.spoj.com/problems/MAY99_2/
/*
  crawl up 5-ary tree
  O(logN base 5)
*/

#include <bits/stdc++.h>
using namespace std;
#define ll long long

string s = "manku";

void solve(ll n) {
	vector<char> v;
	while (n > 0) {
		ll x = n % 5;
		x = (x + 4) % 5;
		v.push_back(s[x]);
	 	--n; n /= 5;
	}
	for (ll i = v.size() - 1; i >= 0; --i)
		cout << v[i];
	cout << "\n";
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	ll t; cin >> t;
	while (t--) {
		ll n; cin >> n;
		solve(n);
	}

	return 0;
}
