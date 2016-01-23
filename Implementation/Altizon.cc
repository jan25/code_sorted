/*
  2d grid. sum of sub matrix.
  binary search for cube of number.
*/

#include <bits/stdc++.h>
using namespace std;

const long long maxn = 1000;
long long g[maxn][maxn];
long long sums[maxn][maxn];
long long n, k;

long long isCube(long long x) {
	long long l = 1, r = (long long)1e6;
	while (r > l) {
		long long mid = (l + r ) / 2;
		long long cmid = mid * mid * mid;
		if (cmid >= x) r = mid;
		else l = mid + 1;
	}
	return r * r * r == x;
}

long long topSum(long long x, long long y) {
	if (x >= 0 && y >= 0)
		return sums[x][y];
	return 0;
}

long long sumSeg(long long ax, long long ay, long long bx, long long by) {
	return topSum(ax, ay) + topSum(bx - 1, by - 1)
			- topSum(ax, by - 1) - topSum(bx - 1, ay);
}

void solve() {
	for (long long i = 0; i < n; ++i) {
		long long lsum = 0;
		for (long long j = 0; j < n; ++j) {
			lsum += g[i][j];
			sums[i][j] += (i ? sums[i - 1][j] : 0) + lsum;
		}
	}

	long long ans = 0;
	for (long long i = k - 1; i < n; ++i) {
		for (long long j = k - 1; j < n; ++j) {
			ans += isCube(sumSeg(i, j, i - k + 1, j - k + 1));
		}
	}
	cout << ans << endl;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> k;
	for (long long i = 0; i < n; ++i)
		for (long long j = 0; j < n; ++j)
			cin >> g[i][j];
	solve();

	return 0;
}
