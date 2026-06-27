# Solution for LeetCode problem "Populating Next Right Pointers in Each Node".

# Description:
#   You are given a perfect binary tree where all leaves are on the same level,
#   and every parent has two children. The binary tree has the definition:
#   struct Node {
#      int val;
#      Node *left;
#      Node *right;
#      Node *next;
#   }
#   Popluate each next pointer to point to its next right node. If there is no
#   next right node, the next pointer should be set to NULL. Initially all pointers
#   are set to NULL.

# Constraints:
#  - Number of nodes in tree range from [0, 2^12 - 1]
#  - -1000 <= Node.val <= 1000

# Complexity:
# - Time: O(n)
# - Space: O(1)

"""
# Definition for a Node.
class Node:
   def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
      self.val = val
      self.left = left
      self.right = right
      self.next = next
"""

def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
  """
  Connects next right pointers in a perfect binary tree.
  """
  if not root:
    return None

  # Start with leftmost node of current level
  leftmost = root

  # Iterate level by level (excluding leaf node)
  while leftmost.left:
    current = leftmost

    # Traverse nodes in the current level
    while current:
      # 1. Connect left child to right child
      current.left.next = current.right

      # 2. Connect right child to next node's left child (if exists)
      if current.next:
        current.next.right = current.next.left

      # Move to the next node in same level
      current = current.next

    # Move to next level
    leftmost = leftmost.left

  return root
