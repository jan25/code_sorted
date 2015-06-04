// flloyd warshall
// n src and 1 dest

#include <bits/stdc++.h>
using namespace std;
#define iOS ios::sync_with_stdio(0)
#define sf scanf
#define pf printf
#define push_back pb
#define make_pair m

#define LL long long

int n, en, T;

const int N = 101;
int d[N][N];

void solve() {
	for (int k = 0; k < N; ++k) {
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (d[i][k] + d[k][j] < d[i][j])
					d[i][j] = d[i][k] + d[k][j];
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < N; ++i) {
		if (d[i][en] <= T) ++ans;
	}
	cout << ans;
}

const int inf = 1e9;

int main() {
	cin >> n >> en >> T;
	int e; cin >> e;
	int a, b, c;
	memset(d, -1, sizeof(d));
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			d[i][j] = inf;
	for (int i = 0; i < N; ++i)
		d[i][i] = 0;
	while (e--) {
		cin >> a >> b >> c;
		d[a][b] = c;
	}
	solve();

	return 0;
}
