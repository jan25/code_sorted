#include <bits/stdc++.h>
using namespace std;

#define EVEN ((v.size() - i) % 2 == 0)

vector<int> v;

int DP[10][2][50][50];

void push_digs(string& a) {
  v.clear();
  for (int i = 0; i < a.length(); ++i)
    v.push_back(a[i] - '0');
}

int dp(int i = 0, int e = 1, int os = 0, int es = 0) {
  if (i == v.size()) return es - os == 1;
  if (DP[i][e][os][es] != -1) return DP[i][e][os][es];
  int c = 0;
  for (int d = 0; d < 10; ++d) {
    if (e && d > v[i]) break;
    c += dp(i + 1, e && (d == v[i]), os + (EVEN ? 0 : d), es + (EVEN ? d : 0));
  }
  return DP[i][e][os][es] = c;
}

int is_raone(string& s) {
  int es, os;
  es = os = 0;
  for (int i = 1; i <= s.length(); ++i) {
    if (i % 2) os += s[s.length() - i] - '0';
    else es += s[s.length() - i] - '0';
  }
  return es - os == 1;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  int tc; cin >> tc;
  while (tc--) {
    string a, b;
    cin >> a >> b;
    push_digs(a);
    memset(DP, -1, sizeof(DP));
    int a_count = dp();
    push_digs(b);
    memset(DP, -1, sizeof(DP));
    int b_count = dp();
    cout << (b_count - a_count + is_raone(a)) << endl;
  } 

  return 0;
}