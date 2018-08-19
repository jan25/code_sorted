/**
 * iterate of subsets of a mask
 */
#include <bits/stdc++.h>
using namespace std;

void print_bin(int n) {
  vector<int> bits;
  while (n > 0) {
    bits.push_back(n & 1);
    n >>= 1;
  }
  reverse(bits.begin(), bits.end());
  for (int i = 0; i < bits.size(); ++i)
    cout << bits[i];
}

void print_subsets(int n) {
  for (int i = n; i > 0; i = (i - 1) & n) {
    cout << (i) << endl;
    cout << ' '; print_bin(i); cout << endl;
  }
}

int main() {

  print_subsets(1000);
  print_bin(1000);

  return 0;
}