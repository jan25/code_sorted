#include <iostream>
#include <cstdlib>
using namespace std;

// prototypes
void print(int* , int);
bool is_sorted(int* a, int n);

/************************************* SELECTION SORT ***********************/
// pass array and size of array (n)
// returns a pair of integers- swaps and comparisions done
pair<int, int> selection_sort(int array[], int n) {
  int count_swaps = 0;
  int count_comp = 0;

  int min_index; // holds index of minimum integer in each selection
  for (int i = 0; i < n - 1; ++i) {
    min_index = i;
    for (int j = i + 1; j < n; ++j) {
      if (array[min_index] > array[j]) {
        // lower integer found. so we update index of mininum integer
        min_index = j;
      }
      count_comp++; // increment for each comparision
    }

    // if minimum is not a index i we need to swap
    if (min_index != i) {
      swap(array[min_index], array[i]);
      count_swaps++;
    }
  }

  return pair<int, int>(count_swaps, count_comp);
}


/************************************* BUBBLE SORT **************************/
pair<int, int> bubble_sort(int array[], int n) {
  int count_swaps = 0;
  int count_comp = 0;

  // Algorithm: bubble the maximum to right end of array
  for (int i = n - 2; i >= 0; --i) {
    // loop to bubble the maximum to right
    for (int j = 0; j <= i; ++j) {
      if (array[j] > array[j + 1]) {
        swap(array[j], array[j + 1]);
        count_swaps++; // swap if right element < left element at index j
      }
      count_comp++; // one comparision needed for each pair- j and j+1
    }
  }

  return pair<int, int>(count_swaps, count_comp); 
}

/************************************* INSERTION SORT ***********************/
pair<int, int> insertion_sort(int array[], int n) {
  int count_swaps = 0;
  int count_comp = 0;

  for (int i = 1; i < n; ++i) {
    // insert element at index i in correct position in array
    int j = i;
    while (j > 0) {
      count_comp++;
      if (array[j] >= array[j - 1]) {
        break; // break if element is inserted in sorted position
      }
      count_swaps++; // swap with left element
      swap(array[j], array[j - 1]);
      --j;
    }
  }

  return pair<int, int>(count_swaps, count_comp); 
}


/************************************* MERGE SORT ***************************/
pair<int, int> merge_sort_recursive(int array[], int l, int r, int temp[]);

pair<int, int> merge_sort(int array[], int n) {
  int temp[n];
  return merge_sort_recursive(array, 0, n - 1, temp); 
}

// recursive merge sort
// pass array to sort, left index, right index, temperorary array
pair<int, int> merge_sort_recursive(int array[], int l, int r, int temp[]) {
  // return (0, 0) for single element array
  if (r - l < 1) return pair<int, int>(0, 0); 

  int mid = (l + r) / 2;
  pair<int, int> p1 = merge_sort_recursive(array, l, mid, temp);
  pair<int, int> p2 = merge_sort_recursive(array, mid + 1, r, temp);

  int count_swaps = p1.first + p2.first; // from left half + right half
  int count_comp = p1.second + p2.second;

  // merge right and left half
  int li = l;
  int ri = mid + 1;
  int tempi = 0;
  while (li <= mid && ri <= r) {
    count_comp++;
    if (array[li] < array[ri]) {
      count_swaps++;
      temp[tempi] = array[li];
      li++;
      tempi++;
    }
    else {
      count_swaps++;
      temp[tempi] = array[ri];
      ri++;
      tempi++;
    }
  }

  while (li <= mid) {
    temp[tempi] = array[li];
    count_swaps++;
    tempi++;
    li++;
  }

  while (ri <= r) {
    temp[tempi] = array[ri];
    count_swaps++;
    tempi++;
    ri++;
  }

  // copy back elements from temp to array
  for (int i = 0, j = l; j <= r; ++i, ++j) {
    array[j] = temp[i];
  }

  return pair<int, int>(count_swaps, count_comp);  
}


/************************************* QUICK SORT ***************************/
// prototype
pair<int, int> quick_sort_recursive(int array[], int l, int r);

pair<int, int> quick_sort(int array[], int n) {
  return quick_sort_recursive(array, 0, n - 1);
}

// recursive quick sort
// pass array, left index and right index in array
pair<int, int> quick_sort_recursive(int array[], int l, int r) {
  int count_swaps = 0;
  int count_comp = 0;

  // sort if more than one element
  if (l < r) {
    int pivot = array[r]; // chose pivot as right most element

    // partitiion array around pivot
    int li = l - 1;
    int ri = l;
    while (ri < r) {
      count_comp++;
      if (array[ri] < pivot) {
        count_swaps++;
        li++;
        swap(array[li], array[ri]);
      }
      ri++;
    }

    int mid = li + 1; // pivot index
    if (mid != r) {
      swap(array[mid], array[r]);
      count_swaps++;
    }

    // recurse left of and right of pivot
    pair<int, int> p1 = quick_sort_recursive(array, l, mid - 1);
    pair<int, int> p2 = quick_sort_recursive(array, mid + 1, r);


    count_swaps += p1.first + p2.first;
    count_comp += p1.second + p2.second;
  }

  return pair<int, int>(count_swaps, count_comp);
}

/************************************* HEAP SORT ****************************/
pair<int, int> heap_sort(int array[], int n) {
  int count_swaps = 0;
  int count_comp = 0;

  // build maxheap in place in array
  for (int i = 1; i < n; ++i) {
    int j = i;
    int parent;
    while (j > 0) {
      count_comp++;
      parent = (j - 1) / 2; // parent index of index j in heap
      if (array[parent] >= array[j]) break;
      swap(array[parent], array[j]);
      count_swaps++;
      j = parent;
    }
  }

  // remove max from heap and put at right end of array
  int right = n - 1;
  while (right > 0) {
    swap(array[right], array[0]); // delete max from heap
  
    count_swaps++;
    right--;

    int i = 0;
    while (i <= right) {
      int left_child = 2 * i + 1;
      int right_child = 2 * i + 2;

      if ((left_child > right || array[left_child] <= array[i]) && 
          (right_child > right || array[right_child] <= array[i])) {
        break;
      }

      int swap_with = left_child;
      count_comp++;
      if (right_child <= right && array[right_child] > array[left_child]) {
        swap_with = right_child;
      }

      swap(array[swap_with], array[i]);
      count_swaps++;
      i = swap_with;
    }
  } 

  return pair<int, int>(count_swaps, count_comp);
}

/*********** UTILITY FUNCTIONS ******************/
// print array a of size n
void print(int* a, int n) {
  for (int i = 0; i < n; ++i)
    cout << a[i] << " ";
  cout << endl;
}

// checks if array a is sorted
bool is_sorted(int* a, int n) {
  for (int i = 1; i < n; ++i)
    if (a[i] < a[i - 1]) return false;
  return true;
}

void copy_array(int* dest, int* src, int n) {
  for (int i = 0; i < n; ++i)
    dest[i] = src[i];
}

/************ MAIN ******************************/
int main() {

  int n = 5000; // size of array

  int array[n];
  
  // random numbers in [0, 5000)
  for (int i = 0; i < n; ++i) {
    array[i] = rand() % 5000;
  }

  int temp[n]; // temporary array to copy used in different sorting calls
  
  // fill sorted array
  copy_array(temp, array, n);
  quick_sort(temp, n);
  int sorted[n];
  for (int i = 0; i < n; ++i)
    sorted[i] = temp[i];

  // fill reverse sorted array
  int reverse_sorted[n];
  for (int i = 0; i < n; ++i)
    reverse_sorted[n - i - 1] = temp[i];

  pair<int, int> p; // pair of integers

  // run selection sort
  cout << "SELECTION SORT: " << endl;
  copy_array(temp, array, n);
  p = selection_sort(temp, n);
  cout << "\t\t random array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, sorted, n);
  p = selection_sort(temp, n);
  cout << "\t\t sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, reverse_sorted, n);
  p = selection_sort(temp, n);
  cout << "\t\t reverse sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;

  // run bubble sort
  cout << "BUBBLE SORT: " << endl;
  copy_array(temp, array, n);
  p = bubble_sort(temp, n);
  cout << "\t\t random array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, sorted, n);
  p = bubble_sort(temp, n);
  cout << "\t\t sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, reverse_sorted, n);
  p = bubble_sort(temp, n);
  cout << "\t\t reverse sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;

  // run insertion sort
  cout << "INSERTION SORT: " << endl;
  copy_array(temp, array, n);
  p = insertion_sort(temp, n);
  cout << "\t\t random array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, sorted, n);
  p = insertion_sort(temp, n);
  cout << "\t\t sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, reverse_sorted, n);
  p = insertion_sort(temp, n);
  cout << "\t\t reverse sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;


  // run merge sort
  cout << "MERGE SORT: " << endl;
  copy_array(temp, array, n);
  p = merge_sort(temp, n);
  cout << "\t\t random array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, sorted, n);
  p = merge_sort(temp, n);
  cout << "\t\t sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, reverse_sorted, n);
  p = merge_sort(temp, n);
  cout << "\t\t reverse sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;

  // run quick sort
  cout << "QUICK SORT: " << endl;
  copy_array(temp, array, n);
  p = quick_sort(temp, n);
  cout << "\t\t random array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, sorted, n);
  p = quick_sort(temp, n);
  cout << "\t\t sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, reverse_sorted, n);
  p = quick_sort(temp, n);
  cout << "\t\t reverse sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;

  // run heap sort
  cout << "HEAP SORT: " << endl;
  copy_array(temp, array, n);
  p = heap_sort(temp, n);
  cout << "\t\t random array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, sorted, n);
  p = heap_sort(temp, n);
  cout << "\t\t sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;
  copy_array(temp, reverse_sorted, n);
  p = heap_sort(temp, n);
  cout << "\t\t reverse sorted array: swaps = " << p.first << " comparisions = " << p.second << endl;


  return 0;
}
