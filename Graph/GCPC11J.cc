/*
      longest path in tree graph; diameter in tree
*/
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define iOS ios::sync_with_stdio(0);

const int N = 1e5 + 7;

vector<int> adj[N];

int h[N];

int mlen(int i, int p) {	
	int hl = 0, hr = 0;
	int maxlen = 0;
	for (int j = 0; j < adj[i].size(); ++j) {
		if (p != adj[i][j]) {
			maxlen = max(maxlen, mlen(adj[i][j], i));
			if (h[adj[i][j]] + 1 >= hr) {
				hl = hr; 
				hr = h[adj[i][j]] + 1;
			}
			else if (h[adj[i][j]] + 1 > hl) hl = h[adj[i][j]] + 1;
		}
	}
	h[i] = hr > hl ? hr : hl;
	return max(maxlen, hr + hl);
}

int main() {
	iOS;
	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		for (int i = 0; i < n; ++i) adj[i].clear();
		while (--n) {
			int a, b; cin >> a >> b;
			adj[a].pb(b);
			adj[b].pb(a);
		}
		int l = mlen(0, -1);
		cout << (l+1)/2 << "\n";
	}

	return 0;
}
