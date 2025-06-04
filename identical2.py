class Node:
    def _init_(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))
    return False

root1=Node(1)
root1.left = Node(2)
root1.right = Node(3)
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print(are_identical(root1, root2)) 