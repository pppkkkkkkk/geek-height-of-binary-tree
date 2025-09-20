'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        
        def dfs(node):
            if node.left and node.right:
                return max(1+dfs(node.left), 1+dfs(node.right))
            elif node.left:
                return 1+dfs(node.left)
            elif node.right:
                return 1+dfs(node.right)
            return 0
            
        return dfs(root)