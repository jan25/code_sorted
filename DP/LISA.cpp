/**
 *    Date: 21.04.2015 
 * 
 */
// top down. memoized.
//
#include <bits/stdc++.h>
using namespace std;
#define isc(c) (c == '*' || c == '+' || (c >= '0' && c <= '9'))
#define gc getchar_unlocked

typedef long long ll;

const ll inf = LONG_MAX;
const int N = 100;

int num[N];
char op[N];
int L;

ll DP[N][N][2]; // 0 min 1 max

void dp(int i, int j) {
	if (i < 0 || j > L) return;
	if (DP[i][j][0] != -1 && DP[i][j][1] != -1) return;
	if (i == j) {
		DP[i][i][1] = DP[i][i][0] = num[i];
		return;
	}
	ll mina = inf, maxa = -1;
	char o;
	for (int k = i+1; k <= j; ++k) {
		dp(i, k-1);
		dp(k, j);
		o = op[k];
		if (o == '*') {
			mina = min(mina, DP[i][k-1][0] * DP[k][j][0]);
			maxa = max(maxa, DP[i][k-1][1] * DP[k][j][1]);
		}
		else {
			mina = min(mina, DP[i][k-1][0] + DP[k][j][0]);
			maxa = max(maxa, DP[i][k-1][1] + DP[k][j][1]);
		}
	}
	DP[i][j][0] = mina;
	DP[i][j][1] = maxa;
}

int main() {
	int t; cin >> t;
	int a, b;
	while (t--) {
		char c = gc();
		while (!isc(c)) c = gc();
		b = 0;
		a = 1;
		while (isc(c)) {
			if (c >= '0' && c <= '9') num[b++] = c - 48;
			else op[a++] = c;
			c = gc();
		}
		L = a-1;
		
		memset(DP, -1, sizeof(DP));
		dp(0, L);		
		
		cout << DP[0][L][1] << ' ' << DP[0][L][0] << "\n";
	}

	return 0;
}
