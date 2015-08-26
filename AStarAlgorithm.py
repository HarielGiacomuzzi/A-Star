import sys
import math
from common import *

class AStarAlgorithm:

	def __init__(self, mapMatrix, playerX,playerY, goalX, goalY, map_width, map_height):
		self.nodesVisited = []
		self.nodesInQueue = []
		self.CaminhoFinal = []
		self.playerPosX = playerX
		self.playerPosY = playerY
		self.goalX = goalX
		self.goalY = goalY
		self.startNode = None
		self.finalNode = None
		self.maxTree = 0
		self.mapMatrix = mapMatrix
		self.map_width = map_width
		self.map_height = map_height
		#pass

	#get the node from the list with the minimum distance 
	def getMinQueue(self):
		auxMin = self.nodesInQueue[0]
		for x in self.nodesInQueue:
			if(x.distance < auxMin.distance):
				auxMin = x
		return auxMin

	#returns the distance from the player to the goal in a straight line 
	def calculateDistance(self,goalX,goalY,playerX,playerY):
		#return math.sqrt(math.pow((goalX-playerX),2) + math.pow((goalY-playerY),2))
		return  abs((goalX - playerX)) + abs((goalY - playerY))

	# preforms the search in the tree of posibilities
	def aStarSearch(self,goalX, goalY, playerX, playerY):
		self.nodesInQueue.append(Node(self.calculateDistance(goalX,goalY,playerX,playerY),playerX,playerY))
		self.startNode = self.nodesInQueue[0]
		maiorDistancia = sys.maxint
		signal = True
		while self.nodesInQueue:
			actualNode = self.getMinQueue()
			signal = True
			if self.calculateDistance(goalX,goalY,actualNode.posX,actualNode.posY) == 0:
				self.finalNode = actualNode
				break
			self.nodesInQueue.remove(actualNode)
			self.mapMatrix[actualNode.posY][actualNode.posX] = 3
			self.nodesVisited.append(Node(self.calculateDistance(goalX,goalY,actualNode.posX,actualNode.posY),actualNode.posX,actualNode.posY))
			#tests the first position of the right
			if self.mapMatrix[actualNode.posY][actualNode.posX+1] != 1 and self.mapMatrix[actualNode.posY][actualNode.posX+1] != 3 and actualNode.posX+1 < self.map_width:
				distance = self.calculateDistance(goalX,goalY,actualNode.posX+1,actualNode.posY)
				if signal:
					self.maxTree += 1
					signal = False
				node = Node(distance,actualNode.posX+1,actualNode.posY)
				actualNode.children.append(node)
				node.father = actualNode
				#implementing this if for a matter of optimization, if the list is at least kind of ordered the for loop which whill look for the
				#minimun value of heuristic to explore will run faster as it will get the "if" inside to fail and the processor will 
				#uses less time to do operations, if you undo this you will notice a considerable change in the speed of the algorithm
				#soo knowing how things happen inside the processor may help you sometimes :D 
				if distance < maiorDistancia:
					self.nodesInQueue.insert(0,node) 
				else:
					self.nodesInQueue.append(node)
			#tests the first position of the left
			if self.mapMatrix[actualNode.posY][actualNode.posX-1] != 1 and self.mapMatrix[actualNode.posY][actualNode.posX-1] != 3 and actualNode.posX-1 >= 0:
				distance = self.calculateDistance(goalX,goalY,actualNode.posX-1,actualNode.posY)
				node = Node(distance,actualNode.posX-1,actualNode.posY)
				actualNode.children.append(node)
				node.father = actualNode
				if signal:
					self.maxTree += 1
					signal = False
				if distance < maiorDistancia:
					self.nodesInQueue.insert(0,node)  
				else:
					self.nodesInQueue.append(node)
			#tests the position above
			if self.mapMatrix[actualNode.posY+1][actualNode.posX] != 1 and self.mapMatrix[actualNode.posY+1][actualNode.posX] != 3 and actualNode.posY+1 < self.map_height:
				distance = self.calculateDistance(goalX,goalY,actualNode.posX,actualNode.posY+1)
				node = Node(distance,actualNode.posX,actualNode.posY+1)
				actualNode.children.append(node)
				node.father = actualNode
				if signal:
					self.maxTree += 1
					signal = False
				if distance < maiorDistancia:
					self.nodesInQueue.insert(0,node)  
				else:
					self.nodesInQueue.append(node)
			#tests the position below
			if self.mapMatrix[actualNode.posY-1][actualNode.posX] != 1 and self.mapMatrix[actualNode.posY-1][actualNode.posX] != 3 and actualNode.posY-1 >= 0:
				distance = self.calculateDistance(goalX,goalY,actualNode.posX,actualNode.posY-1)
				node = Node(distance,actualNode.posX,actualNode.posY-1)
				actualNode.children.append(node)
				node.father = actualNode
				if signal:
					self.maxTree += 1
					signal = False
				if distance < maiorDistancia:
					self.nodesInQueue.insert(0,node)  
				else:
					self.nodesInQueue.append(node)

	#gets the path in a recursive manner
	def findPathFinal(self, node):
		if node.distance == 0:
			return node
		for child in node.children:
			aux = self.findPathFinal(child)
			if aux != None:
				self.CaminhoFinal.insert(0,aux)
				return child
		return None

	#gets the path now whith a while
	def findPathFinalNotRecursive(self,node):
		while node.father != None:
			self.CaminhoFinal.insert(0,node)
			node = node.father

	#looking if this is solvable, as it runs tooo fast we'll run it :P
	def getSolvable(self):
		if self.finalNode == None:
			self.aStarSearch(self.goalX,self.goalY,self.playerPosX,self.playerPosY)
		return self.finalNode != None

	# the minimal cost to get to the final point
	def getMinCost(self):
		if self.finalNode == None:
			self.aStarSearch(self.goalX,self.goalY,self.playerPosX,self.playerPosY)
		return len(self.CaminhoFinal)-1

	def getMaxTree(self):
		if self.finalNode == None:
			self.aStarSearch(self.goalX,self.goalY,self.playerPosX,self.playerPosY)
		return self.maxTree
	#starts the search and make the procedures needed for getting the list of steps and etc...
	def startSearch(self):
		if self.finalNode == None:
			self.aStarSearch(self.goalX,self.goalY,self.playerPosX,self.playerPosY)
		self.findPathFinalNotRecursive(self.finalNode)
		self.CaminhoFinal.insert(0,self.startNode)
		aux = []
		for i in range(0,len(self.CaminhoFinal)-1):
			print(self.CaminhoFinal[i].posX,self.CaminhoFinal[i].posY,self.CaminhoFinal[i].distance)
		for i in range(0,len(self.CaminhoFinal)-1):
			if self.CaminhoFinal[i].posX < self.CaminhoFinal[i+1].posX:
				aux.append(MOVE_RIGHT)
				continue
			if self.CaminhoFinal[i].posX > self.CaminhoFinal[i+1].posX:
				aux.append(MOVE_LEFT)
				continue
			if self.CaminhoFinal[i].posY > self.CaminhoFinal[i+1].posY:
				aux.append(MOVE_UP)
				continue
			if self.CaminhoFinal[i].posY < self.CaminhoFinal[i+1].posY:
				aux.append(MOVE_DOWN)
				continue
			aux.append(None)
		return aux

# just for make things clear
class Node:
	def __init__(self,distance,posx,posy):
		self.posX = posx
		self.posY = posy
		self.distance = distance
		self.children = []
		self.father = None

