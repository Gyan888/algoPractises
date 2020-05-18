
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class Linklist:
	def __init__(self,node):
		self.head=node

	def printNext(self):
		node=self.head
		while(node.next!=None):
			print ("data :",node.data)
			node=node.next

n1=Node(1)
n2=Node(2)
n3=Node(3)
ls=Linklist(n1)
n1.next=n2
n2.next=n3
n3.next=None
ls.printNext()


