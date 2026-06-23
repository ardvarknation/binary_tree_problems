# Solution 2 for LeetCode "Binary Tree Zigzag Level Order Traversal" problem.
# Uses a two-stack approach.
# Description:
#  Given the root of a binary tree, return the zigzag level order traversal of
#  it's nodes' values (from left to right, then right to left for next level,
#  and so on).

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
  """
  Function to perform zigzag breadth-first traversal on binary tree.
  @args: root, a TreeNode
  @returns: result, a list of int's

  Constraints:
  - The number of nodes in the tree range from [0, 2000]
  - -100 <= Node.val <= 100
  """
  if not root:
    return []

  result = []

  current_level = [root]    # Stack for current level
  leftToRight = True        # Direction flag

  while current_level:
    level = []
    next_level = []

    # Process all nodes in current stack
    while current_level:
      node = current_level.pop()
      level.append(node.val)

      # Push children in order depending on direction
      if leftToRight:
        # Left first, then right
        if node.left:
          next_level.append(node.left)
        if node.right:
          next_level.append(node.right)

        else:
          # Right first, then left
          if node.right:
            next_level.append(node.right)
          if node.left:
            next_level.append(node.left)

    result.append(level)

    # Move to the next level
    current_level = next_level

    # Flip direction 
    leftToRight = not leftToRight

  return result
