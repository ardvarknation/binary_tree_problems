# Solution for LeetCode "Binary Tree Zigzag Level Order Traversal" problem.
# Description:
#  Given the root of a binary tree, return the zigzag level order traversal of
#  it's nodes' values (from left to right, then right to left for next level,
#  and so on).
# Complexity:
# - Time: O(N)
# - Space: O(N)

from collections import deque

def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
  """
  Function to perform zigzag breadth-first traversal on binary tree.
  @args: root, a TreeNode
  @returns: result, a list of int's

  Constraints:
  - The number of nodes in the tree range from [0, 2000]
  - -100 <= Node.val <= 100
  """

  # If the tree is empty, return empty result
  if not root:
    return []

  result = []              # Final result list
  queue = deque([root])    # Queue for BFS
  leftToRight = True       # Flag for direction

  # Perform BFS level by level
  while queue:
    level_size = len(queue)    # Number of nodes in current level
    level = deque()            # Use deque for efficient insertion

    # Process each node in the current level
    for _ in range(level_size):
      node = queue.popleft()  # Remove node from front of queue

      # Insert node value based on traversal direction
      if leftToRight:
        level.append(node.val)      # Normal order
      else:
        level.appendleft(node.val)  # Reverse order
        
      # Add children to queue for next level
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    # Add the completed level to result (convert deque --> list)
    result.append(list(level))

    # Flip direction for next level
    leftToRight = not leftToRight

  return result
