INT_MIN = float("-infinity")
INT_MAX = float("infinity")

class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		super(Node, self).__init__()
		self.data = data
		self.left = None
		self.right = None


class ListNode(object):
	def __init__(self, data):
		super(ListNode, self).__init__()
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		super(LinkedList, self).__init__()
		self.head = None
		
	def push(self, data):
		newNode = ListNode(data)
		newNode.next = self.head
		self.head = newNode


	def printList(self):
		self.printListUtil(self.head)


	def printListUtil(self, node):
		if node is not None:
			print node.data
			self.printListUtil(node.next)

	def length(self):
		node = self.head
		size = 0
		while node is not None:
			size += 1
			node = node.next

		return size



def inorder(root):

	current = root
	s = []
	done = 0

	while not done:

		if current is not None:
			s.append(current)
			current = current.left

		else:
			if(len(s)>0):
				current = s.pop()
				print current.data
				current = current.right

			else:
				done = 1


def levelOrderTraversal(root):

	h = height(root)

	for i in range(1, h+1):
		printLevel(root, i)
		print ""


def printLevel(root, level):

	if root is None:
		return

	if level == 1:
		print root.data,
	else:
		printLevel(root.left, level-1)
		printLevel(root.right, level-1)


def height(root):

	if root is None:
		return 0
	else:
		lheight = height(root.left)
		rheight = height(root.right)

		if lheight > rheight:
			return lheight+1
		else:
			return rheight+1


def findLCA(root, n1, n2):

	if root is None:
		return None

	if root.data in (n1, n2):
		return root


	left_lca = findLCA(root.left, n1, n2)
	right_lca = findLCA(root.rright, n1, n2)


	if(left_lca and right_lca):
		return root

	return left_lca if left_lca is not None else right_lca






def diameter(root):

	if root is None:
		return 0


	lHeight = height(root.left)
	rheight = height(root.right)

	return max(max(diameter(root.left), diameter(root.right)), lHeight+rheight+1)


def numbers(n):
	for i in range(0, n+1):
		print "\"%d\","%(i),


def getPreIndex():
	return constructTreeUtil.index


def incrementPreIndex():
	constructTreeUtil.index += 1

def constructTreeUtil(pre, item, minM, maxM, size):

	if(getPreIndex()>=size):
		return None
	root = None
	if item>minM and item<maxM:


		root = Node(item)
		incrementPreIndex()

		if(getPreIndex()<size):
			root.left = constructTreeUtil(pre, pre[getPreIndex()], minM, item, size)
		if(getPreIndex()<size):
			root.right = constructTreeUtil(pre, pre[getPreIndex()], item, maxM, size)

	return root


def constructTree(pre):
	constructTreeUtil.index = 0	
	return constructTreeUtil(pre, pre[0], INT_MIN, INT_MAX, len(pre))

def sortedListToBST(linkedList):
	length = linkedList.length()	
	return sortedListToBSTUtil(linkedList, length)


def sortedListToBSTUtil(_list, size):


    if size <= 0:
     	return None

    left = sortedListToBSTUtil(_list, size/2)
    root = Node(_list.head.data)
    root.left = left
    _list.head = _list.head.next
    root.right = sortedListToBSTUtil(_list, size-size/2-1)
    return root




linkedList = LinkedList()

linkedList.push(5)
linkedList.push(4)
linkedList.push(3)
linkedList.push(2)
linkedList.push(1)
#linkedList.printList()
#levelOrderTraversal(sortedListToBST(linkedList))

# def createBST(n):
# 	return createBSTUtil(1, n)


def createBSTUtil(a, b):

	roots = []
	if a>b:
		roots.append(None)
		return roots


	for i in range(a, b+1):

		left_roots = createBSTUtil(a, i-1)
		right_roots = createBSTUtil(i+1, b)

		for left_root in left_roots:
			for right_root in right_roots:
				newNode = Node(i)
				newNode.left = left_root
				newNode.right = right_root
				roots.append(newNode)

	return roots

def inorderWREC(root):

	stack = []
	current = root
	while True:

		while current != None:
			stack.append(current)
			current = current.left

		node = stack.pop()
		print node.data
		current = node.right

		if current is None and len(stack) == 0:
			break

def kLargest(k, root):
	stack = []
	current = root
	count = 0
	while True:

		while current != None:
			stack.append(current)
			current = current.left

		node = stack.pop()
		count += 1
		if count == k:
			return node.data
		current = node.right

		if current is None and len(stack) == 0:
			break

# for tree in createBST(4):
# 	levelOrderTraversal(tree)

root = Node(9)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
#inorderWREC(root)
#print kLargest(1, root)


def printString(s, n):
	for i in range(n):
		print s,


def printTringle(n):
	for i in range(1, n+1):
		printString(" ", n-i)
		printString("*", 2*i-1)
		printString(" ", n-i)
		print ""


def printBrokenTringle(righShift, n):
	for i in range(2, n+1):
		printString(" ", righShift +  n-i)
		printString("*", 2*i-1)
		printString(" ", n-i)
		print ""



def printChristmasTree(days):
	maxm = days + 3
	for day in reversed(range(days+1)):
		if day == days:
			printTringle(maxm)
		else:
			printBrokenTringle(days-day, maxm)

		maxm -= 1

	printString(" ", days+2)
	print("*")
	printString(" ", days+2)
	print("*")



def largestBSTUtil(root, data):

	if root is None:
		data['is_bst'] = True
		return 0

	left_flag = False
	right_flag = False

	minM = INT_MAX

	data['max'] = INT_MIN
	leftTreeBSTSize = largestBSTUtil(root.left, data)

	if data['is_bst'] and root.data > data['max']:
		left_flag = True

	minM = data['min']

	data['min'] = INT_MAX
	rightTreeBSTSize = largestBSTUtil(root.right, data)


	if data['is_bst'] and root.data < data['min']:
		right_flag = True

	if data['min'] > minM:
		data['min'] = minM

	if data['min'] > root.data:
		data['min'] = root.data

	if data['max'] < root.data:
		data['max'] = root.data


	if left_flag and right_flag:
		if (leftTreeBSTSize + rightTreeBSTSize + 1) > data['max_bst']:
			data['max_bst'] = leftTreeBSTSize + rightTreeBSTSize + 1
		data['is_bst'] = True
		return leftTreeBSTSize + rightTreeBSTSize + 1

	else: 
		data['is_bst']= False
		return 0

def largestBST(root):
	data ={'min':INT_MIN, 'max': INT_MAX, 'max_bst':0, 'is_bst':False}
	largestBSTUtil(root, data)
	return data['max_bst']

#printChristmasTree(5)


# root = Node(9)
# root.left = Node(2)
# root.right = Node(4)
# root.left.left = Node(1)
# root.left.right = Node(3)



def mergeBST(root1, root2):

	stack1 = []
	current1 = root1

	stack2 = []
	current2 = root2
	while True:

		while current1 != None:
			stack1.append(current1)
			current1 = current1.left


		while current2 != None:
			stack2.append(current2)
			current2 = current2.left

		if len(stack1)!=0 and (len(stack2) == 0 or stack1[-1].data < stack2[-1].data):
			node = stack1.pop()
			print node.data
			current1 = node.right
		else:
			node = stack2.pop()
			print node.data
			current2 = node.right

		if current1 is None and len(stack1) == 0 and current2 is None and len(stack2) == 0:
			break

root = Node(50)
root.left = Node(30)
root.right = Node(60)
root.left.left = Node(5)
root.left.right = Node(20)
root.right.left = Node(45)
root.right.right = Node(70)
root.right.right.left = Node(65)
root.right.right.right = Node(80)
#print largestBST(root)


root1 = Node(100)
root1.left = Node(30)
root1.right = Node(300)
root1.left.left = Node(20)
root1.left.right = Node(70)


root2 = Node(80)
root2.left = Node(40)
root2.right = Node(120)


mergeBST(root1, root2)



3 9 12 56 30 58 


8, 58, 71, 18, 31, 32, 63, 92, 
         43, 3, 91, 93, 25, 80, 28



    28
25      80
          93
     91



   91 

25   93

  80

28
