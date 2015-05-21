#include <bits/stdc++.h>
using namespace std;
#define pb push_back

const int N = 5001;

int n, m;

vector<int>* adj;
vector<int>* adjt;

int v[N];

int noc;

stack<int> s;

int comp[N];

void dfs(int i) {
	if (v[i]) return;
	v[i] = 1;
	vector<int>::iterator it = adj[i].begin();
	while (it != adj[i].end()) {
		dfs(*it);	
		++it;
	}
	s.push(i);
}

set<int> sink;

void dfs2(int i) {
	comp[i] = noc;
	v[i] = 1;
	vector<int>::iterator it = adjt[i].begin();
	while (it != adjt[i].end()) {
		if (!v[*it]) dfs2(*it);
		else if (comp[*it] != noc) sink.insert(comp[*it]);
		++it;
	}
}

void solve() {
	memset(v, 0, sizeof(v));	
	for (int i = 1; i <= n; ++i) dfs(i);

	memset(v, 0, sizeof(v));
	sink.clear();
	noc = 1;
	while (!s.empty()) {
		int i = s.top();
		dfs2(i);
		while (!s.empty() && v[s.top()]) {
			s.pop();
		}
		++noc;
	}
	for (int i = 1; i <= n; ++i) {
		if (sink.find(comp[i]) == sink.end()) cout << i << ' ';
	}
	cout << "\n";
}

int main() {
	ios::sync_with_stdio(0);
    freopen("input.txt", "r+", stdin);
    freopen("output.txt", "w+", stdout);
	
	cin >> n;
	while (n) {
		adj = new vector<int>[n+1];
		adjt = new vector<int>[n+1];
		cin >> m;
		int a, b;
		for (int i = 0; i < m; ++i) {
			cin >> a >> b;
			adj[a].pb(b);
			adjt[b].pb(a);
		}
		solve();
		cin >> n;
	}
	return 0;
}
