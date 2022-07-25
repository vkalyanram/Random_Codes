class Market:
	def __init__(self, owned):
		self.owned = owned
		self.total=100
		self.shares=[]
		self.share_value=[]
		self.owner=None
		self.percentage=100

	def add_share(self,owning,percentage):
			owning.owner=self
			owning.percentage=percentage
			owning.total=self.total*percentage/100
			self.shares.append(owning)
			self.share_value.append(owning.total)

	def get_level(self):
		    level = 0
		    p = self.owner
		    while p:
			    level += 1
			    p = p.owner

		    return level

	def print_tree(self):
		spaces = ' ' * self.get_level() * 3
		prefix = spaces + "|__" if self.owner else ""
		postfix = " "+"("+ str(self.total)+")"+" "+"Each Share & Values "+ str(self.share_value) if self.total else ""
		print(prefix + self.owned+postfix)
		if self.shares:
			for share in self.shares:
				share.print_tree()






"""
	def company_shares_list(self):
		return self.shares

	def shares_total_value(self):
		value=[]
		[value.append(i.total) for i in self.shares]
		return sum(value)		

	def share_missing_value(self):
		
		if self.shares:
			share_value=[]
			[share_value.append(i.total) for i in self.shares]
			d=int(self.total-sum(share_value))
		else:
			d=0
		return d

	def net_missing_percentage(self,var):
		return int(self.total*(net_missing_value/100))
	
"""   
"""f = open('sample/in_01.txt', 'r')
Lines = f.readlines()
company=""
for line in Lines:	
	commands=line.strip().split(" ")
	company_name=commands[0]
	company_share=commands[1]
	company_share_per=commands[2]
	if len(company)==0:
		company=company_name
		obj=Market(commands[0])
	if company==commands[0]:
		if commands[1] not in obj.shares: obj.add_share(Market(commands[1]),int(commands[2])) 



mismatch=[]
if obj.company_shares_list():
	[mismatch.append(i.share_missing_value()) for i in obj.shares]
mismatch_shares=sum(mismatch)
total_share_value=obj.shares_total_value()
net_missing_value=obj.total-total_share_value+mismatch_shares
out_put=""
if net_missing_value==0:
	for i in obj.shares:
		out_put=out_put+company+" "+i.owned+" "+str(i.percentage)+"\n"
else:  
	for i in obj.shares:
		out_put=out_put+company+" "+i.owned+" "+str(i.percentage)+"\n"  
	o=company+" "+"?"+" "+str(obj.net_missing_percentage(net_missing_value))+"\n"
	out_put=o+out_put

print(out_put)"""
################################## python3.8 run_tests.py python3.8 ./Market.py ####################
### Intermediate owners

company=Market("a")
b=Market("b")
company.add_share(b,50)
c=Market("c")
company.add_share(c,40)
d=Market("d")
company.add_share(d,10)
e=Market("e")
b.add_share(e,50)
f=Market("f")
b.add_share(f,50)
f1=Market("f1")
d.add_share(f1,100)
company.print_tree()