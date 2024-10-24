
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    """ The algorithm 

       The algorithm uses recursion to solve the problem of checking whether two binary trees are flip equivalent.

        The idea is to compare corresponding nodes in root1 and root2.
             First, we check if the current nodes in both trees are equal:
                If they are, we proceed to compare the left and right subtrees.
                If they are not, we attempt to compare the left subtree of one tree with the right subtree of the other.

        The recursion continues until all nodes are checked.

        The trees are considered flip equivalent if either:
            The left and right subtrees of both roots are equivalent.
            The left subtree of one root is equivalent to the right subtree of the other (i.e., after a flip).
        If both conditions fail, the trees are not flip equivalent, and the function returns False.



    

    """
    
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 or not root2 :
            return not root1 and not root2
        
        if root1.val != root2.val :
            return False
        

        sameside = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        differentside = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)


        return sameside or differentside
        