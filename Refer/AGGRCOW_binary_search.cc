// http://www.spoj.com/problems/AGGRCOW/
/*
	binary search [over possible answer space]
	O(n * log(max(xi)))
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 7;
int ar[maxn];
int n, c;

int solve() {
	int l = 1;
	int r = (int)1e9;
	while (l < r) {
		int mid = (l + r + 1) / 2;
		int next = 0;
		int done = c;
		for (int i = 0; i < n; ++i) {
			if (ar[i] >= next) {
				--done;
				next = ar[i] + mid;
			}
		}
		if (done <= 0) l = mid;
		else r = mid - 1;
	}
	return r;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	
	int t; cin >> t;
	while (t--) {
		cin >> n >> c;
		for (int i = 0; i < n; ++i) cin >> ar[i];
		sort(ar, ar + n);
		cout << solve() << "\n";
	}

	return 0;
}
