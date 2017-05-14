class TreeNode:
	def __init__(self, x):
		self.key = x
		self.marked = True #initiate in tango searching
		self.aux = None #initiate in tango searching
		self.parent = None
		self.prefer = None # preferred child, initiate in tango searching
		self.repreLeft = None # left child in representative tree, initiate in tango
		self.repreRight = None # right child in representative tree, initiate in tango
		self.left = None # left child in auxiliary tree, initiate in splay tree
		self.right = None # right child in auxiliary tree, initiate in splay tree
