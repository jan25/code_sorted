/*
	segment tree. lazy idea
	co-ordinates compressed
*/

#include <bits/stdc++.h>
using namespace std;
#define mid (l + r)/2

const int N = 40000;
int lazy[6*N];

vector<int> m;
vector<pair<int, int> > qs;
int n;
map<int, int> se;
set<int> s;



void pass(int i, int l, int r) {
	if (lazy[i]) {
		lazy[2*i + 1] = lazy[2*i + 2] = lazy[i];
	}
	lazy[i] = 0;
}

void update(int x, int y, int v, int i = 0, int l = 0, int r = n - 1) {
	if (x > r || y < l) return ;
	if (x <= l && y >= r) {
		lazy[i] = v;
		return ;
	}
	pass(i, l, r);
	update(x, y, v, 2*i + 1, l, mid);
	update(x, y, v, 2*i + 2, mid + 1, r);
}

void gocount(int i = 0, int l = 0, int r = n - 1) {
	if (lazy[i]) {
		s.insert(lazy[i]);
		return ;
	}
	if (r - l < 1) return ;
	gocount(2*i + 1, l, mid);
	gocount(2*i + 2, mid + 1, r);
}


int main() {
	ios::sync_with_stdio(0);
	int t; cin >> t;
	int a, b;
	while (t--) {
		n = 0;
		m.clear();
		qs.clear();
		int q; cin >> q;
		while (q--) {
			cin >> a >> b;
			m.push_back(a); m.push_back(b);
			qs.push_back(make_pair(a, b));
		}
		sort(m.begin(), m.end());
		n = m.size();
		se.clear();
		int c = 0;
		for (int i = 0; i < n; ++i) {
			if (se.find(m[i]) == se.end()) 
				se[m[i]] = c++;
		}
		n = c;
		q = qs.size();
		memset(lazy, 0, sizeof(lazy));
		for (int i = 0; i < q; ++i) {
			a = qs[i].first;
			b = qs[i].second;
			update(se[a], se[b], i + 1);
		}
		s.clear();
		gocount();
		cout << s.size() << "\n";
	}

	return 0;
}
