class Node(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 


def flattern(tree):
    if not tree or ( not tree.left  and not tree.right):
        return 
    if tree.left :
        flattern(tree.left)
        temp = tree.right
        tree.right = tree.left
        tree.left = None 
        t = tree.right 
        while t.right:
            t = t.right 
        t.right = temp 
        flattern(tree.right)

testTree = Node(1)
testTree.left = Node(2)
testTree.right = Node(5)
testTree.left.left = Node(3)
testTree.left.right = Node(4)
testTree.right.right = Node(6)
flattern(testTree)

while testTree:
    print (testTree.val)
    testTree = testTree.right 


