# Solution to LeetCode "Inorder Binary Tree Traversal" problem.
# Iterative version.
# Description:
#   Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Complexity:
# - Time: O(n)
# - Space: O(h)

def inorderTraversal(self, root: Optional[ListNode]) -> List[int]:
  """
  Function to iteratively perform DFS on binary tree.

  @args: root, a binary tree node
  @returns: ans, a List

  Constraints:
  - The number of nodes in the tree range from [0, 100]
  - -100 <= Node.val <= 100
  """
  stack = []        # stack to simulate recursion
  ans = []          # result list
  current = root    # start from root

  # Continue while there are nodes to process
  while current or stack:

    # Step 1: Go as far LEFT as possible
    while current:
      stack.append(current)  # save node to come back later
      current = current.left

    # Step 2: Process the node
    current = stack.pop()    # get last saved node
    ans.append(current.val)  # "visit" the node

    # Step 3: Move to RIGHT subtree
    current = current.right

  return ans
    
