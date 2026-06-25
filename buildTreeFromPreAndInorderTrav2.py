# Solution 2 for the LeetCode "Construct Binary Tree from Preorder and Inorder Traversals" problem.
# Description: 
#   Given two integer arrays - preorder and inorder - where preorder is the preorder traversal of a 
#   binary tree and inorder is the inorder traversal of the same tree, construct and return the 
#   binary tree.

# Constraints:
# - 1 <= preorder.length <= 3000
# - inorder.length == preorder.length
# - -3000 <= preorder[i], inorder[i] <= 3000
# - preorder and inorder consist of unique values
# - Each value of inorder also appears in preorder
# - preorder is guaranteed to be the preorder traversal of the tree
# - inorder is guaranteed to be the inorder traversal of the tree

# Complexity:
# - Time: O(n) as each node is processed once
# - Space: O(n) as stack is used

# Definition for a Binary Tree node
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Constructs a binary tree from preorder and inorder traversal lists iteratively,
    using a stack to simulate recursion.

    @param: preorder, List[int] - preorder traversal (root -> left -> right)
    @param: inorder, List[int] - inorder traversal (left -> root -> right)
    @return: TreeNode - root of reconstructed binary tree
    """

    # Edge case: if traversal lists/arrays are empty
    if not preorder or not inorder:
      return None

    # Step 1: Create the root node from the first preorder element
    root = TreeNode(preorder[0])

    # Stack will be used to simulate recursion
    stack = [root]

    # Pointer to track position in inorder traversal
    inorder_index = 0

    # Step 2: Iterate over remaining preorder values
    for i in range(1, len(preorder)):
      current_val = preorder[i]

      # The top of the stack is the last created node
      node = stack[-1]

      # Case 1: The top of the stack is NOT equal to current inorder value
      # -> We are still traversing down the left subtree
      if node.val != inorder[inorder_index]:
        # Create a new node and attach it as LEFT child
        node.left = TreeNode(current_val)

        # Push the new node onto the stack
        stack.append(node.left)

      else:
        # Case 2: The stack top matches inorder -> we've finished the LEFT subtree
        # We need to backtrack (pop until a mismatch)
        while stack and stack[-1].val == inorder[inorder_index]:
          node = stack.pop()
          inorder_index += 1      # Move forward in inorder

        # Now we are ready to attach the RIGHT child
        node.right = TreeNode(current_val)

        # Push the new node
        stack.append(node.right)

    # Final constructed tree root
    return root
