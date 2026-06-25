# Solution 1 for the LeetCode "Construct Binary Tree from Preorder and Inorder Traversals" problem.
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
# - Time: O(n) 
# - Space: O(log n) in best case, when tree balanced; O(n) in worst case, when tree skewed

# Definition for a Binary Tree node
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Constructs a binary tree from preorder and inorder traversal lists recursively.

    @param: preorder, List[int] - preorder traversal (root -> left -> right)
    @param: inorder, List[int] - inorder traversal (left -> root -> right)
    @return: TreeNode - root of reconstructed binary tree
    """

    # Step 1: Build a hashmap for quick lookup of inorder indices
    # This allows you to find the root position in O(1) time
    inorder_map = {value: idx for idx, value in enumerate(inorder)}

    # Step 2: Define recursive helper function
    def build(pre_start, pre_end, in_start, in_end):
      """
      Recursive helper function for building binary tree.

      @param: pre_start - start index in preorder
      @param: pre_end - end index in preorder
      @param: in_start - start index in inorder
      @param: in_end - end index in inorder
      """

      # Base case: if there are no elements to construct the subtree
      if pre_start > pre_end or in_start > in_end:
        return None

      # Step 3: First element in preorder is the root
      root_val = preorder[pre_start]
      root = TreeNode(root_val)

      # Step 4: Find the root index in inorder traversal
      in_root_index = inorder_map[root_val]

      # Step 5: Calculate the number of nodes in the left subtree
      left_size = in_root_index - in_start

      # Step 6: Recursively build the left subtree
      root.left = build(
        pre_start + 1,            # next element of preorder
        pre_start + left_size,    # end of left subtree in preorder
        in_start,                 # start of left subtree in inorder
        in_root_index - 1         # end of the left subtree in inorder
      )

      # Step 7: Recursively build the right subtree
      root.right = build(
        pre_start + left_size + 1,  # start of right subtree in preorder
        pre_end,                    # end of current subtree in preorder
        in_root_index + 1,          # start of right subtree in inorder
        in_end                      # end of right subtree in inorder
      )

      # Step 8: Return constructed subtree root
      return root

    # Initial call: full range of both arrays
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

