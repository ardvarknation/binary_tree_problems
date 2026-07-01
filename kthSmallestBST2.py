# Solution 2 (iterative using stack) for LeetCode problem "K-th Smallest Element in a BST".
# Description:
#   Given the root of a binary search tree, and an integer k, return the k-th smallest
#   value (1-indexed) of all the values of the nodes in the tree.

# Constraints:
# - The number of nodes in tree is n
# - 1 <= k <= n <= 10^4
# - 0 <= Node.val <= 10^4

# Complexity:
# - Time: O(h + k) best case, O(n) in worst case
# - Space: O(h)

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
    stack = []
    current = root

    while True:
      # Go as far left as possible
      stack.append(current)
      current = current.left

    # Process the node
    current = stack.pop()
    k -= 1

    # If k becomes 0, the result is found
    if k == 0:
      return current.val

    # Move to right subtree
    current = current.right
    
