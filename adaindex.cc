#include <bits/stdc++.h>
using namespace std;

const int N = 1e6 + 16;
int trie[N][26][2]; // next, count
int f = 1;

void trie_put(string& s) {
  int i = 0;
  int ti = 0;
  for (int i = 0; i < s.length(); ++i) {
    int c = s[i] - 'a';
    if (trie[ti][c][0] == 0) {
      trie[ti][c][0] = f;
      f++;
    }
    trie[ti][c][1]++;
    ti = trie[ti][c][0];
  }
}

int trie_query(string& s) {
  int ti = 0;
  for (int i = 0; ; ++i) {
    int c = s[i] - 'a';
    if (trie[ti][c][1] == 0) return 0;
    if (i == s.length() - 1) return trie[ti][c][1];
    ti = trie[ti][c][0];
  }
}


int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  int n; cin >> n;
  int q; cin >> q;
  while (n--) {
    string s; cin >> s;
    trie_put(s);
  }

  while (q--) {
    string s; cin >> s;
    cout << trie_query(s) << endl;
  }

  return 0;
}