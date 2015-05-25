/*
    date 25 05 2015
    stat wa
*/
//  segmented sieve. linear time


#include <bits/stdc++.h>
using namespace std;

typedef long long int;

const int N = 1e6 + 10;

int m, n;

int primes[N];

void print() {
	memset(primes, 0, sizeof(primes));
	if (m == 1) primes[0] = 1;
	for (int i = 2; i * i <= n; ++i) {
		int j;
		if (i * i >= m) j = i * i;
		else {
			j = m / i;
			while (j * i < m) ++j;
			j = j * i;
		}
		for (; j <= n; j += i) {
			primes[j - m] = 1;
		}
	}
	for (int i = m; i <= n; ++i) {
		if (!primes[i - m]) 
			printf("%d\n", i);
	}
}

int main() {
	int t; scanf("%d", &t);
	while (t--) {
		scanf("%d %d", &m, &n);
		print();
	}

	return 0;
}
