/*
  Impl: Treap data structure*
  Expected logN for insert, delete and search
  Treap == BST + heap property
  *Not generic. keys can be int only
*/

struct treap {

  struct node {
    int key;
    int priority;
    node* left;
    node* right;
  };

  node* t;

  treap() : t(NULL) { }

  void insert(int a) {
    rec_insert(&t, a);
  }

  node* rec_insert(node** root, int a) {
    if (*root == NULL) *root = new_node(a);
    else if ((*root)->key > a) {
      rec_insert(&((*root)->left), a);
    }
    else {
      rec_insert(&((*root)->right), a);
    }
    *root = balance(*root);
  }

  node* balance(node* root) {
    if (root->left != NULL && root->left->priority > root->priority)
      return rotate_right(root);
    if (root->right != NULL && root->right->priority > root->priority)
      return rotate_left(root);
    return root;
  }

  node* rotate_right(node* root) {
    if (root == NULL || root->left == NULL) return root;
    node* temp = root;
    root = root->left;
    temp->left = root->right;
    root->right = temp;
    return root;
  }

  node* rotate_left(node* root) {
    if (root == NULL || root->right == NULL) return root;
    node* temp = root;
    root = root->right;
    temp->right = root->left;
    root->left = temp;
    return root;
  }

  void remove(int a) {
    node** ptr = search(&t, a);
    if (*ptr == NULL) return ;
    int inf = 1e9 + 19;
    (*ptr)->priority = -inf;
    rec_remove(ptr);
  }

  void rec_remove(node** ptr) {
    if (*ptr == NULL || (*ptr)->priority > 0) return ;
    if (leaf(*ptr)) {
      free(*ptr);
      *ptr = NULL;
      return ;
    }
    *ptr = balance(*ptr);
    rec_remove(&((*ptr)->right));
    rec_remove(&((*ptr)->left));
  }

  bool found(int a) {
    node** ptr = search(&t, a);
    return *ptr != NULL;
  }

  node** search(node** root, int a) {
    if (*root == NULL || (*root)->key == a) return root;
    if (a < (*root)->key) return search(&((*root)->left), a);
    return search(&((*root)->right), a);
  }

  bool leaf(node* n) {
    return n != NULL && (n->left == NULL && n->right == NULL);
  }

  node* new_node(int a) {
    node* a_node = (node*)malloc(sizeof(node));
    a_node->key = a;
    a_node->priority = rand();
    a_node->left = a_node->right = NULL;
    return a_node;
  }

};
