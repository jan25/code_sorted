/*
	date: 20 05 2015
*/

//4 x 4 matrix exp 

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll mod = 1e9 + 7;

ll start[4][4] = {{1, 1, 1, 1}, {1, 0, 0, 0},
					{0, 1, 0, 0}, {0, 0, 1, 0}};

ll tmp[4][4];

void mul(ll A[4][4], ll B[4][4]) {
	ll cell;
	for (ll i = 0; i < 4; ++i) {
		for (ll j = 0; j < 4; ++j) {
			cell = 0;
			for (ll a = 0; a < 4; ++a) {
				cell += (A[i][a]*B[a][j])%mod;
				cell %= mod;
			}
			tmp[i][j] = cell;
		}
	}
	memcpy(A, tmp, 16*sizeof(ll));
}

void power(ll T[4][4], ll n) {
	if (n == 0 || n == 1) return;
	power(T, n/2);
	mul(T, T);
	if (n%2) mul(T, start);
}

ll tetra(ll n) {
	if (n <= 2) return 0;
	if (n == 3) return 1;
	
	ll T[4][4];
	memcpy(T, start, 16*sizeof(ll));
	power(T, n - 3);

	return T[0][0];
}

ll sum(ll m) {
	return (3*tetra(0) + 2*tetra(1) + tetra(2) - tetra(4) +
				tetra(m + 4) - 2*tetra(m + 1) - tetra(m + 2) + mod)%mod; 
}

int main() {
	ios::sync_with_stdio(0);
	
	ll t; cin >> t;
	while (t--) {
		ll n, m; cin >> n >> m;
		cout << ((((sum(m) - sum(n - 1) + mod) % mod) * 333333336) % mod) << "\n";
	}

	return 0;
}
