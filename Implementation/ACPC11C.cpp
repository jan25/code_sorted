
#include <bits/stdc++.h>
using namespace std;

const int N = 1e5;
const int inf = INT_MAX;

int pre[N+1];

int main() {
	ios::sync_with_stdio(0);
	int t, a; cin >> t;
	while (t--) {
		cin >> a;
		pre[0] = 0;
		for (int i = 1; i <= a; ++i) {
			cin >> pre[i];
			pre[i] += pre[i-1];
		}
		int ans = inf;
		for (int i = 1; i <= a; ++i) {
			ans = min(ans, pre[a]-pre[i] + 2*pre[i-1]);
			ans = min(ans, pre[i-1] + 2*(pre[a]-pre[i]));
		}
		cout << ans << "\n";
	}

	return 0;
}
