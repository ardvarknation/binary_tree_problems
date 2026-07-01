import java.util.Stack;

public class kthSmallestBSTIterative {

  public class kthSmallestBSTIterative(TreeNode root, int k) {
    Stack<TreeNode> stack = new Stack<>();
    TreeNode current = root;

    while (true) {
      // Go to the leftmost node
      while (current != null) {
        stack.push(current);
        current = current.left;
      }

      // Process node
      current = stack.pop();
      k--;

      // If k == 0, smallest value has been found
      if (k == 0) {
        return current.val;
      }

      // Move to right subtree
      current = current.right;
    }
  }
}
