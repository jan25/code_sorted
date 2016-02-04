/*
 Suffix Array DS. O(Nlog2N) time for construction using qs
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 7;
int sufar[20][maxn];

struct e {
	int f, s, t;
} L[maxn];

int n;

bool comp(struct e a, struct e b) {
	return (a.f == b.f) ? (a.s < b.s) : (a.f < b.f);
}

int sa[maxn];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s; cin >> s;
	n = s.length();
	for (int i = 0; i < n; ++i) {
		sufar[0][i] = s[i] - 'a';
	}
	int st = 1, don = 1;
	while (don < n) {
		for (int i = 0; i < n; ++i) {
			L[i].f = sufar[st - 1][i];
			L[i].s = i + don < n ? sufar[st - 1][i + don] : -1;
			L[i].t = i;
		}
		sort(L, L + n, comp);
		for (int i = 0; i < n; ++i) {
			sufar[st][L[i].t] = (i > 0 && L[i].f == L[i - 1].f && L[i].s == L[i - 1].s) ? sufar[st][L[i - 1].t] : i;
		}
		++st;
		don <<= 1;
	}
	--st;
	for (int i = 0; i < n; ++i) {
		sa[sufar[st][i]] = i;
	}
	for (int i = 0; i < n; ++i) {
		for (int j = sa[i]; j < n; ++j)
			cout << s[j];
		cout << endl;
	}

	return 0;
}
