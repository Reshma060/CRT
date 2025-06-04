class Node:
    def _init_(self,data):
        self.left=None
        self.right=None
        self.data=data
class BST:
    def _init_(self):
        self.root=None
    def insert(self,data,root):
        # if root==empty:
        # starting point of a tree
        if(root is None):
            return Node(data)
        # if data<root-> left rcc call
        if(data<root.data):
            root.left=self.insert(data,root.left)
        elif(data.root.data):
            root.right=self.insert(data,root.right)
        return root
    def inorder_traversal(self,root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data,end=" ")
            self.inorder_traversal(root.right)
    def preorder_traversal(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    def postorder_traversal(self,root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data,end=" ")
bst_tree=BST()
root=None
bst_tree.insert(20,root)
bst_tree.insert(30,root)
bst_tree.insert(39,root)
bst_tree.insert(100,root)
bst_tree.inorder_traversal(root)
bst_tree.preorder_traversal(root)
bst_tree.postorder_traversal(root)