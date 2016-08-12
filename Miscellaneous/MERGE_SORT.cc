/*
  Merge sort Impl: Recursive and Iterative
  Iterative Impl: using bottom up technique through length of sub arrays
*/
#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

// merge two halves [l, mid] and [mid + 1, r]
void merge(int a[], int l, int mid, int r, int temp[]) {
  int tempi = 0;
  int li = l;
  int ri = mid + 1;
  while (li <= mid && ri <= r) {
    if (a[li] < a[ri]) {
      temp[tempi] = a[li];
      li++;
      tempi++;
    }
    else {
      temp[tempi] = a[ri];
      ri++;
      tempi++;
    }
  }
  while (li <= mid) {
    temp[tempi] = a[li];
    tempi++;  
    li++;
  }
  while (ri <= r) {
    temp[tempi] = a[ri];
    tempi++;
    ri++;
  }
  for (int i = l, j = 0; j < tempi; ++i, ++j) {
    a[i] = temp[j];
  }
}

/*******************************ITERATIVE*************************************/

// iterative merge sort
void merge_sort_iter(int a[], int n) {
  int temp[n];
  for (int l = 1; l <= n; l <<= 1) {
    for (int i = 0; i + l < n; i += 2 * l) {
      int left = i;
      int mid = i + l - 1;
      int right = min(n - 1, i + 2*l - 1);
      merge(a, left, mid, right, temp);
    } 
  }      
}

/*****************************************************************************/

/*******************************RECURSIVE*************************************/

// recursive helper for merge sort
void merge_sort_solve(int a[], int l, int r, int temp[]) {
  if (l < r) {
    int mid = (l + r) / 2;
    merge_sort_solve(a, l, mid, temp);
    merge_sort_solve(a, mid + 1, r, temp);
    merge(a, l, mid, r, temp);
  }
}

// solve merge sort recursively
void merge_sort_rec(int a[], int n) {
  int temp[n];
  merge_sort_solve(a, 0, n - 1, temp);
}

/*****************************************************************************/

// to check if array a[] is sorted
bool is_sorted(int a[], int n) {
  for (int i = 1; i < n; ++i)
    if (a[i] < a[i - 1]) return false;
  return true;
}

int main() {
  
  /*
    use below lines of code to run for merge sort for different random inputs
    with variable input size
  */

  // used to generate different random numbers each time program is run
  srand(time(NULL)); 


  // below code can be used to time a part of program
  clock_t start = clock(); // get start time

  // perform computation

  clock_t end = clock();

  // calculate time for computation from start to end
  double total_time_for_computation = double(end - start) / CLOCKS_PER_SEC;


  return 0;
}