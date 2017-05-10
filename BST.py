from treenode import TreeNode

class BalancedTree:
	def __init__(self, nodes):
		self.root = self.initiate(nodes)
	
	def initiate(self, nodes):
		if len(nodes) == 0:
			return None
		median = nodes[len(nodes)/2]
		root = TreeNode(median)
		if len(nodes) == 1:
			return root
		smaller = nodes[:len(nodes)/2]
		larger = nodes[len(nodes)/2 + 1:]
		left = self.initiate(smaller)
		right = self.initiate(larger)
		root.left = left
		root.right = right
		return root

tree = BalancedTree([1,2,3,4,5,7,8])
# print tree.root.key
# print tree.root.left.key
# print tree.root.left.right
