#include <bits/stdc++.h>
#define ll long long
using namespace std;

const int N = 1e5 + 1;
ll w[N];
priority_queue<int, vector<int> > q[N];

vector<ll> 


int main() {
  int n; cin >> n;
  for (int i = 0; i < n; ++i)
    cin >> w[i];
  int m; cin >> m;
  while (m--) {
    int op, x, wt; cin >> op;
    if (op == 1) {
      cin >> x >> wt;
      addFarEdge(x, wt);
    } else if (op == 2) {
      cin >> x >> wt;
      addEdge(x, wt); 
    } else if (op == 3) {
      cin >> x;
      deleteFarNode(x);
    } else {
      cin >> x;
      cout << getFarDist(x) << endl;
    }
  }
  
  return 0;
}
