// Definition for a Binary Tree Node
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode(int val) {
    this.val = val;
  }
}

public class kthSmallestBST {
  private int count = 0;    // Tracks how many nodes were visited
  private int result = -1;  // Stores the k-th smallest value

  public int kthSmallest(TreeNode root, int k) {
    inorder(root, k);
    return result;
  }

  private void inorder(TreeNode node, int k) {
    // Base case: stop if node is null or result already found
    if (node == null) {
      return;
    }

    // Traverse the left subtree (smaller values)
    inorder(node.left, k);

    // Visit current node
    count++;

    // If this is the k-th node, store result
    if (count == k) {
      result = node.val;
      return;
    }

    // Traverse right subtree (larger values)
    inorder(node.right, k);

  }
}
