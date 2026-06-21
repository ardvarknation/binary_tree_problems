# Solution to LeetCode "Inorder Binary Tree Traversal" problem.
# Recursive version.
# Description:
#   Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Complexity:
# - Time: O(n)
# - Space: O(h)

def inorderTraversal(self, root: Optional[ListNode]) -> List[int]:
  """
  Function to recursively perform DFS on binary tree.

  @args: root, a binary tree node
  @returns: ans, a List

  Constraints:
  - The number of nodes in the tree range from [0, 100]
  - -100 <= Node.val <= 100
  """
  # Helper function for recursion
  def dfs(node):
    # Check base case: if node is None, return empty list
    if not node:
      return []

    # Recursively traverse:
    # 1. Left subtree
    # 2. Current node
    # 3. Right subtree
    left_values = dfs(node.left)    # all values from left subtree
    current_values = [node.val]     # current node value as a list
    right_values = dfs(node.right)  # all values from right subtree

    # Combine results for inorder traversal
    return left_values + current_values + right_values

  # Start recursion from root
  return dfs(root)
