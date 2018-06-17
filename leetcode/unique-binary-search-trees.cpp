#include <bits/stdc++.h>
using namespace std;

/**
* 1D DP solution
* Counting number of unique bst structures, given number of nodes
* O(N) recursive impl
* WIP
*/

class Solution {

private:
  vector<int> DP;

public:
    int numTrees(int n) {
      // tree(n) = for i in 1..n tree(n - i) * tree(i)
      this->DP.resize(n + 1, -1);
      return this->dp(n);  
    }

    int dp(int n) {
      if (n == 0) return 1;
      if (n < 3) return n;
      if (this->DP[n] != -1) return this->DP[n];
      this->DP[n] = 0;
      for (int i = 0; i <= n; ++i) {
        this->DP[n] += dp(i) * dp(n - i);
        if (n % 2 == 1 and n - i - 1 == i) {
          this->DP[n] -= dp(i);
        }
      }
      return this->DP[n];
    }
};

int main() {
  int n; cin >> n;
  cout << ((new Solution())->numTrees(n)) << endl;

  return 0;
}