#include <bits/stdc++.h>
using namespace std;

const int maxn = 5007;
int x[maxn];
int y[maxn];
int store[maxn];

bool comp(int i, int j) {
	if (x[i] - x[j]) return x[i] < x[j];
	return y[i] < y[j];
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n; cin >> n;
	for (int i = 0; i < n; ++i) {
		store[i] = i;
		cin >> x[i] >> y[i];
	}
	sort(store, store + n, comp);
	int prev = 1;
	for (int i = 0; i < n; ++i) {
		prev = y[store[i]] >= prev ? y[store[i]] : x[store[i]];
	}
	cout << prev << "\n";

	return 0;
}
