from treenode import TreeNode
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = self.right = None

#     def equals(self, node):
#         return self.key == node.key

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = TreeNode(None) #For splay()

    def insert(self, node):
        if not self.root:
            self.root = node
            return

        self.splay(node.key)
        if self.root.key == node.key: # If the key is already there in the tree, don't do anything.
            return

        if node.key < self.root.key:
            node.left = self.root.left
            node.right = self.root
            self.root.left = None
        else:
            node.right = self.root.right
            node.left = self.root
            self.root.right = None
        self.root = node

    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            raise 'key not found in tree'

        # Now delete the root.
        if self.root.left== None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        depth = self.splay(key, True)
        # if self.root.key != key:
        #     return None
        return (self.root, depth)

    def isEmpty(self):
        return self.root == None
    
    def splay(self, key, count=False):
        depth = 0
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
            depth += 1
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t
        if count:
            return depth

    def join(self, S): 
        """
        :param S: splay tree with all nodes larger than current ones
        :return: None
        """
        x = self.findMax()
        self.splay(x)
        self.root.right = S.root


    def split(self, x, inclusive):
        """
        :param x: element in splay tree
        :return:  less than x, one with elements larger than x
        """
        self.splay(x)
        left = self.root.left
        right = self.root.right
        if inclusive:
            self.root.left = None
            if left:
                cur = [left]
            else:
                cur = None
        else:
            self.root.right = None
            if right:
                cur = [right]
            else:
                cur = None
        new = SplayTree()
        while cur:
            next = []
            for item in cur:
                if item and item.left:
                    next += item.left,
                if item and item.right:
                    next += item.right,
            for node in cur:
                new.insert(node)
            cur = next

        return new

    def traversal_test(self):
        if not self.root:
            return None
        cur = [self.root]
        while cur:
            next = []
            for item in cur:
                if item and item.left:
                    next += item.left,
                if item and item.right:
                    next += item.right,
            s = ""
            for i in cur:
                s += (str(i.key) + ",")
            print s
            cur = next



