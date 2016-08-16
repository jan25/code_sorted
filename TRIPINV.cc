#include <bits/stdc++.h>
using namespace std;

struct bit {

  long long* b;
  int n;

  bit(int n) : n(n) {
    b = new long long[n];
  }

  void clear() {
    for (int i = 0; i < n; ++i)
      b[i] = 0;
  }

  void put(int x, long long val) {
    assert(x > 0 && x < n);
    while (x < n) {
      b[x] += val;
      x += x & -x;
    }
  }

  long long get_sum(int x) {
    assert(x > 0 && x < n);
    long long sum = 0;
    while (x > 0) {
      sum += b[x];
      x -= x & -x;
    }
    return sum;
  }

  ~bit() {
    delete[] b;
  }

};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  int maxn = 1e5 + 1;
  long long* ar = new long long[maxn];

  bit b(maxn);

  int n; cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> ar[i];
  }

  b.clear();

  long long* inv = new long long[n];
  for (int i = n - 1; i >= 0; --i) {
    inv[i] = ar[i] > 1 ? b.get_sum(ar[i] - 1) : 0;
    b.put(ar[i], 1);
  }  

  b.clear();

  long long ti = 0;
  for (int i = n - 1; i >= 0; --i) {
    ti += ar[i] > 1 ? b.get_sum(ar[i] - 1) : 0;
    b.put(ar[i], inv[i]);
  }

  cout << ti << "\n";

  delete[] inv;
  delete[] ar;

  return 0;
}