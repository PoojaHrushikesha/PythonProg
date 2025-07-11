class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    """
    Check if a binary tree is a valid Binary Search Tree (BST).
    A BST is defined as:
    - The left subtree of a node contains only nodes with values less than the node's value.
    - The right subtree of a node contains only nodes with values greater than the node's value.
    - Both the left and right subtrees must also be BSTs.
    """
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        
        val = node.val
        if val <= lower or val >= upper:
            return False
        
        if not helper(node.right, val, upper):
            return False
        if not helper(node.left, lower, val):
            return False
        
        return True
    
    return helper(root)

# Helper function to create a binary tree from a list
def create_tree_from_list(lst, index=0):
    if index >= len(lst) or lst[index] is None:
        return None
    root = TreeNode(lst[index])
    root.left = create_tree_from_list(lst, 2*index + 1)
    root.right = create_tree_from_list(lst, 2*index + 2)
    return root

# Test cases
if __name__ == "__main__":
    # Test Case 1: Valid BST
    #     2
    #    / \
    #   1   3
    tree1 = create_tree_from_list([2, 1, 3])
    print("Test Case 1 (Valid BST):", is_valid_bst(tree1))  # Expected: True
    
    # Test Case 2: Invalid BST
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    tree2 = create_tree_from_list([5, 1, 4, None, None, 3, 6])
    print("Test Case 2 (Invalid BST):", is_valid_bst(tree2))  # Expected: False
    
    # Test Case 3: Single node
    tree3 = create_tree_from_list([1])
    print("Test Case 3 (Single node):", is_valid_bst(tree3))  # Expected: True
    
    # Test Case 4: Empty tree
    tree4 = create_tree_from_list([])
    print("Test Case 4 (Empty tree):", is_valid_bst(tree4))  # Expected: True
    
    # Test Case 5: Invalid BST with duplicate values
    #     2
    #    / \
    #   2   2
    tree5 = create_tree_from_list([2, 2, 2])
    print("Test Case 5 (Duplicate values):", is_valid_bst(tree5))  # Expected: False
    
    # Test Case 6: Valid complex BST
    #         8
    #        / \
    #       3   10
    #      / \    \
    #     1   6    14
    #        / \   /
    #       4   7 13
    tree6 = create_tree_from_list([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13])
    print("Test Case 6 (Complex valid BST):", is_valid_bst(tree6))  # Expected: True
