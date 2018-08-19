/**
* nice BFS
* http://www.spoj.com/problems/ESJAIL/
*/

#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 7;
vector<int> g[maxn];
int vis[maxn];
int door[maxn];
int key[maxn];
int n, k, m;

void pushNeighbors(queue<int>& q, int v) {
  for (int i = 0; i < g[v].size(); ++i) {
    if (!vis[g[v][i]]) {
      vis[g[v][i]] = 1;
      q.push(g[v][i]);
    }
  }  
}

string bfs() {
  memset(vis, 0, sizeof(vis));
  queue<int> q;
  q.push(1);
  vis[1] = 1;
  while (!q.empty()) {
    int v = q.front();
    if (v == n) return "Y";
    q.pop();
    if (!door[v]) {
      pushNeighbors(q, v);
      if (key[v] && vis[key[v]]) pushNeighbors(q, key[v]);
    }
    else if (vis[door[v]]) pushNeighbors(q, v);
  }
  return "N";
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  while (1) {
    cin >> n >> k >> m;
    if (n == -1) break;
    memset(door, 0, sizeof(door));
    memset(key, 0, sizeof(key));
    for (int i = 0; i < k; ++i) {
      int a, b; cin >> a >> b;
      door[b] = a;
      key[a] = b;
    }
    for (int i = 1; i <= n; ++i)
      g[i].clear();
    while (m--) {
      int a, b; cin >> a >> b;
      g[a].push_back(b);
      g[b].push_back(a);
    }
    cout << bfs() << endl;
  } 

  return 0;
}
