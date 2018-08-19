/*
  min heap array implementation
*/

#include <bits/stdc++.h>
using namespace std;

typedef struct heap {

	/* min heap */

	int ar[(int)1e6 + 7];
	int freei = 0;

	bool isEmpty() {
		return !freei;
	}

	int getMin() {
		return isEmpty() ? INT_MAX : ar[0];
	}

	int par(int i) {
		int rem = i % 2;
		return rem == 0 ? i / 2 - 1 : i / 2;
	}

	int push(int val) {
		ar[freei] = val;
		int i = freei;
		while (i && ar[i] < ar[par(i)]) {
			swap(ar[i], ar[par(i)]);
			i = par(i);
		}
		++freei;
	}

	bool leaf(int i) {
		return freei <= 2 * i + 1;
	}

	int getLeft(int i) {
		i = 2 * i + 1;
		return ar[i];
	}

	int getRight(int i) {
		i = 2 * i + 2;
		return i >= freei ? INT_MAX : ar[i];
	}

	int pop() {
		if (isEmpty()) return INT_MAX;
		int x = getMin();
		int i = 0;
		ar[0] = ar[freei - 1];
		--freei;
		while (!leaf(i)) {
			int left = getLeft(i);
			int right = getRight(i);
			if (left >= ar[i] && right >= ar[i]) break;
			int j;
			if (left <= right) {
				j = 2 * i + 1;
				swap(ar[i], ar[j]);
			}
			else {
				j = 2 * i + 2;
				swap(ar[i], ar[j]);
			}
			i = j;
		}
		return x;
	}

} heap;

int main() {
		
	int n = 10;
		
	heap h;
	for (int i = 0; i < n; ++i) {
		int x = rand() % n;
		h.push(x);
		cout << x << " ";
	}	
	cout << "\n";

	while (!h.isEmpty())
		cout << h.pop() << " ";
	cout << "\n";

	return 0;
}
