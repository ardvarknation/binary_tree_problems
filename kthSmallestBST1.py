# Solution 1 (using recursion) for LeetCode problem "K-th Smallest Element in a BST".
# Description:
#   Given the root of a binary search tree, and an integer k, return the k-th smallest
#   value (1-indexed) of all the values of the nodes in the tree.

# Constraints:
# - The number of nodes in tree is n
# - 1 <= k <= n <= 10^4
# - 0 <= Node.val <= 10^4

# Complexity:
# - Time: O(h + k) best case, O(n) in worst case
# - Space: O(h) due to recursion

# Definition for a Binary Tree Node
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    """
    Finds the k-th smallest element in a BST using in-order traversal.

    :param root: TreeNode - root of the BST
    :param k: int - the rank of the smallest element to find
    :return: int - the k-th smallest value
    """
    # Variable to store the result
    result = None

    # Counter to track how many nodes have been visited
    counter = 0

    # Define recursive in-order traversal function
    def inorder(node):
      nonlocal count, result

      # Base case: if node is None, stop recursion
      if not node:
        return

      # Traverse left subtree (smaller values)
      inorder(node.left)

      # Visit the current node
      counter += 1

      # If the k-th node is reached, store result
      if counter == k:
        result = node.val
        return

      # Traverse the right subtree (larger values)
      inorder(node.right)

    # Start in-order traversal at the root
    inorder(root)

    return result
