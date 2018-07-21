
from collections import defaultdict
from Queue import Queue
import numpy as np


INT_MAX = float("infinity")


def static_var(variable, value):
	def decorator(func):
		setattr(func, variable, value)
		return func
	return decorator

class Edge(object):
	"""docstring for Edge"""
	def __init__(self, src, des, weight):
		super(Edge, self).__init__()
		self.weight = weight
		self.src = src
		self.des = des


class Graph:

	def __init__(self, **kargs):

		if  'edges' not in kargs:
			self.graph = defaultdict(list)
			self.size = kargs['vertices']
			self.matrix = None
		else:
			self.edge_count = kargs['edges']
			self.size = kargs['vertices']
			self.edges = []



	def addEdge(self, *args):

		if len(args) == 2:
			self.graph[args[0]].append(args[1])
		elif len(args) == 3:
			self.edges.append(Edge(args[0], args[1], args[2]))

	def addUndirectedEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def DFSUtil(self, v, visited):
		visited[v] = True
		print v
		for adjV in self.graph[v]:
			if not visited[adjV]:
				self.DFSUtil(adjV, visited)

	def DFS(self, v):
		visited = [False]*(self.size)
		self.DFSUtil(v, visited)

	def topologicSortUtil(self, v, visited, stack):
		
		visited[v] = True

		for adjV in self.graph[v]:
			if not visited[v]:
				self.topologicSortUtil(adjV, visited, stack)

		stack.append(v)

	def topologicSort(self):
		visited = [False]*(self.size)
		stack = []

		for vertex in range((self.size)):
			if not visited[vertex]:
				self.topologicSortUtil(vertex, visited, stack)

		stack.reverse()
		print stack

	def nextState(self, a, b, state):

		possibleStates = []

		if state[0] == 0:
			possibleStates.append( (a, state[1]) )

		if state[1] == 0:
			possibleStates.append( (state[0], b) )

		state1 = [state[0], state[1]]
		state2 = [state[0], state[1]]

		for water in range(1, max(a, b)+1):

			state1[0] -= 1
			state1[1] += 1


			if( (state1[0] == 0 and state1[1] <=b) or (state1[1] == b and state1[0]>=0) ):
				possibleStates.append( tuple(state1) )

			state2[0] += 1
			state2[1] -= 1


			if( (state2[0] <=a and state2[1] == 0 ) or (state2[0] == a and state2[1] >=0 ) ):
				possibleStates.append( tuple(state2) )

		possibleStates.append( (state[0], 0) )
		possibleStates.append( (0, state[1]) )

		return possibleStates

	def printPath(self, map, state):

		if state == (-1, -1):
			return

		print state
		self.printPath(map, map[state])

	def waterJug(self, a, b, target):

		map = {}
		q = Queue()
		q.put((0, 0))
		map[(0, 0)] = (-1, -1)
		while not q.empty():
			state = q.get()
			if state[0] == target or state[1] == target:
				self.printPath(map, state)
				break
			for s in self.nextState(a, b, state):
				if s not in map.keys():
					map[s] = state
					q.put(s)

	def detectCycleUtil(self, v, visited, recStack):
		
		visited[v] = True
		recStack[v] = True

		for adjV in self.graph[v]:
			if not visited[adjV] and self.detectCycleUtil(adjV, visited, recStack):
				return True
			elif recStack[adjV] == True:
				return True

		recStack[v] = False
		return False


	def detectCycle(self):

		visited = [False]*self.size
		recStack = [False]*self.size

		for vertex in range(self.size):
			if not visited[vertex]:
				if self.detectCycleUtil(vertex, visited, recStack) == True:
					return True

		return False


	def detectCycleUndirectedUtil(self, v, prev, visited):
		
		visited[v] = True

		print v, prev
		for adjV in self.graph[v]:
			if not visited[adjV]:
				if self.detectCycleUndirectedUtil(adjV, v, visited):
					return True
			elif adjV != prev:
				return True

		return False


	def detectCycleUndirected(self):

		visited = [False]*self.size

		for vertex in range(self.size):
			if not visited[vertex]:
				if self.detectCycleUndirectedUtil(vertex, -1,  visited) == True:
					return True

		return False

	def printMST(self, parent):

		for v in range(1, self.size):
			print parent[v], "-", v, self.matrix[parent[v]][v]


	def primMST(self):
		
		key = [INT_MAX]*self.size
		mstSet = [False]*self.size
		parent = [-1]*self.size
		key[0] = 0
		parent[0] = -1

		for vertex in range(self.size-1):
			print key
			u = np.argmin(key)
			mstSet[u] = True
			key[u] = INT_MAX

			for v in range(self.size):
				if self.matrix[u][v] != 0 and mstSet[v] == False and self.matrix[u][v] < key[v]:
					print v, self.matrix[u][v]
					key[v] = self.matrix[u][v]
					parent[v] = u


		self.printMST(parent)


	def find(self, subsets, i):
		if subsets[i]['parent'] != i:
			return self.find(subsets, subsets[i]['parent'])

		return i


	def union(self, subsets, x, y):
		xroot = self.find(subsets, x)
		yroot = self.find(subsets, y)

		if subsets[xroot]['rank'] < subsets[yroot]['rank']:
			subsets[xroot]['parent'] = yroot

		elif subsets[xroot]['rank'] > subsets[yroot]['rank']:
			subsets[yroot]['parent'] = xroot

		else:
			subsets[yroot]['parent'] = xroot
			subsets[xroot]['rank'] += 1

	def borukaMST(self):
		
		cheapest = [-1]*self.size
		subsets = [{'parent': i, 'rank': 0} for i in range(self.size)]

		numTress = self.size
		mstWeight = 0

		while numTress > 1:
			cheapest = [-1]*self.size

			for i, edge in enumerate(self.edges):
				set1 = self.find(subsets, edge.src)
				set2 = self.find(subsets, edge.des)		

				if set1 == set2:
					continue

				else:
					if cheapest[set1] == -1 or self.edges[cheapest[set1]].weight > edge.weight:
						cheapest[set1] = i
					if cheapest[set2] == -1 or self.edges[cheapest[set2]].weight > edge.weight:
						cheapest[set2] = i


			for v in range(self.size):
				set1 = self.find(subsets, self.edges[cheapest[v]].src)
				set2 = self.find(subsets, self.edges[cheapest[v]].des)


				if set1 == set2:
					continue

				mstWeight += self.edges[cheapest[v]].weight
				print self.edges[cheapest[v]].src, self.edges[cheapest[v]].des
				self.union(subsets, set1, set2)

				numTress -= 1

		print mstWeight


	def testing(self):

		a = defaultdict(Edge)

		a[0] = Edge(0, 1, 41)
		print a

	def isSafe(self, row, column):

		for i in range(column):
			if self.matrix[row][i] == 1:
				return False


		i = row
		j = column
		while i >=0 and j>=0:
			if self.matrix[i][j] == 1:
				return False
			i -=1 
			j -=1


		i = row
		j = column
		while i < self.size and j>=0:
			if self.matrix[i][j] == 1:
				return False
			i +=1 
			j -=1

		return True

	def solveNQUtil(self, column):
		if column >= self.size:
			return True

		for i in range(self.size):
			if self.isSafe(i, column):
				self.matrix[i][column] = 1

				if self.solveNQUtil(column+1) == True:
					return True

				self.matrix[i][column] = 0


		return False





	def solveNQ(self):
		if self.solveNQUtil(0) == False:
			print "No Solution exits"
		else:
			print self.matrix

	def APUtil(self, u, parent, visited, ap, disc, low):


		children = 0
		visited[u] = True
		disc[u] =  self.time
		low[u] = self.time
		self.time += 1

		for v in self.graph[u]:

			if not visited[v]:
				children += 1
				parent[v] = u
				self.APUtil(v, parent, visited, ap, disc, low)
				low[u] = min(low[u], low[v])


				if parent[u] is None and children > 1 :
					ap[u] = True



				if parent[u] is not None and low[v] >= disc[u]:
					ap[u] = True

			elif v != parent[u]:
				low[u] = min(disc[v], low[u])






	def ArticulationPoint(self):
		parent = [None]*self.size
		visited = [False]*self.size
		disc = [INT_MAX]*self.size
		low = [INT_MAX]* self.size
		ap = [False]*self.size
		self.time = 0
		for vertex in range(self.size):
			if not visited[vertex]:
				self.APUtil(vertex, parent, visited, ap, disc, low)


		for i in range(self.size):
			if ap[i] == True:
				print i


# g = Graph(vertices=5)
# g.matrix = [[0, 2, 0, 6, 0],
#                       [2, 0, 3, 8, 5],
#                       [0, 3, 0, 0, 7],
#                       [6, 8, 0, 0, 9],
#                       [0, 5, 7, 9, 0],
#                      ]
#g.primMST()


# g = Graph(vertices=4, edges=5)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0 ,3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)

# #g.borukaMST()





# g = Graph(vertices=5)
# g.matrix = [[0]*5 for i in  range(5)]
# g.solveNQ()

#g.testing()
# g = Graph(3)
# g.addUndirectedEdge(0, 1)
# g.addUndirectedEdge(1, 2)
# g.addUndirectedEdge(2, 0)
# #g.DFS(5)


# #g.waterJug(30, 25, 15)
# print g.detectCycleUndirected()


g1 = Graph(vertices=5)
g1.addUndirectedEdge(1, 0)
g1.addUndirectedEdge(0, 2)
g1.addUndirectedEdge(2, 1)
g1.addUndirectedEdge(0, 3)
g1.addUndirectedEdge(3, 4)
g1.ArticulationPoint()



# atix.applyandinitiate D/Main: Name Value pair inputIntent:avr
# 05-23 16:13:11.113 14124-14124/com.ultimatix.applyandinitiate D/Main: Name Value pair inputAttribute:type
# 05-23 16:13:11.113 14124-14124/com.ultimatix.applyandinitiate D/Main: Name Value pair inputSentence:Today
# 05-23 16:13:11.113 14124-14124/com.ultimatix.applyandinitiate D/Main: raw null  
# 05-23 16:13:11.113 14124-14124/com.ultimatix.applyandinitiate D/requestBody: {"timezone":"Asia\/Calcutta","inputIntent":"avr","inputAttribute":"type","inputSentence":"Today"}
# 05-23 16:13:11.113 14124-14124/com.ultimatix.applyandinitiate D/request url: http://10.56.32.21:8080/UltimatixAIBOT/AIBotAttributeIdentifier


