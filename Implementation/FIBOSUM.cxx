/*
**	date: 20 05 2015
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll mod = 1e9 + 7;

ll start[2][2] = {{1, 1}, {1, 0}};

void mul(ll res[2][2], ll A[2][2], ll B[2][2]) {
	ll x = A[0][0]*B[0][0] + A[0][1]*B[1][0];
	ll y = A[0][0]*B[0][1] + A[0][1]*B[1][1];
	ll a = A[1][0]*B[0][0] + A[1][1]*B[0][1];
	ll b = A[1][0]*B[0][1] + A[1][1]*B[1][1];
	res[0][0] = x%mod;
	res[0][1] = y%mod;
	res[1][0] = a%mod;
	res[1][1] = b%mod;
}

void exp(ll n, ll F[2][2]) {
	if (n == 0 || n == 1) return;
	exp(n/2, F);
	mul(F, F, F);
	if (n%2) {
		mul(F, F, start);
	}
}

ll fib(ll n) {
	if (n <= 0) return 0;
	
	ll F[2][2];
	memcpy(F, start, 4*sizeof(ll));
	exp(n - 1, F);
	return F[0][0];
}

int main() {
	ll t; cin >> t;
	while (t--) {
		ll n, m; cin >> n >> m;
		cout << (mod + fib(m + 2) - fib(n + 1)) % mod << "\n";
	}

	return 0;
}
