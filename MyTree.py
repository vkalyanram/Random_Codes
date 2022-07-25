class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, data):
		self.data=data
		self.parent=None
		self.children=[]
	def add(self,child):
		child.parent=self
		self.children.append(child)
	def get_level(self):
	    level=0
	    p=self.parent
	    while p:
	        level+=1
	        p=p.parent
	    return level    		
	def tree(self):
		s=" "*self.get_level()*3
		p=s+"|__" if self.parent else ""
		
		print(p+self.data)
		for i in self.children:
			i.tree()

root=TreeNode("Electronics")
	
l=TreeNode("Laptop")
l.add(TreeNode("Mac"))
l.add(TreeNode("LINUX"))
l.add(TreeNode("Win"))	
m=TreeNode("Mob")
m.add(TreeNode("S"))
m.add(TreeNode("VIVO"))
t=TreeNode("TV")
t.add(TreeNode("Onida"))
t.add(TreeNode("Mi"))	
root.add(l)
root.add(m)
root.add(t)
root.tree()
