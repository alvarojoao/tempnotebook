#!/usr/bin/python
from collections import OrderedDict
import sys
pacman_r = 35
pacman_c = 35
food_r = 35
food_c = 1
r = 37
c = 37
grid = ['%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%','%-------%-%-%-----------%---%-----%-%','%-%%%%%%%-%-%%%-%-%%%-%%%-%%%%%%%-%-%','%-------%-------%-%-----%-----%-%---%','%%%%%-%%%%%-%%%-%-%-%-%%%-%%%%%-%-%%%','%---%-%-%-%---%-%-%-%---%-%---%-%---%','%-%%%-%-%-%-%%%-%%%%%-%%%-%-%%%-%%%-%','%-------%-----%---%---%-----%-%-%---%','%%%-%%%%%%%%%-%%%%%%%-%%%-%%%-%-%-%-%','%-------------%-------%-%---%-----%-%','%-%-%%%%%-%-%%%-%-%-%%%-%-%%%-%%%-%-%','%-%-%-----%-%-%-%-%-----%---%-%-%-%-%','%-%-%-%%%%%%%-%-%%%%%%%%%-%%%-%-%%%-%','%-%-%-%-----%---%-----%-----%---%---%','%%%-%%%-%-%%%%%-%%%%%-%%%-%%%-%%%%%-%','%-----%-%-%-----%-%-----%-%---%-%-%-%','%-%-%-%-%-%%%-%%%-%%%-%%%-%-%-%-%-%-%','%-%-%-%-%-----------------%-%-%-----%','%%%-%%%%%%%-%-%-%%%%%-%%%-%-%%%-%%%%%','%-------%-%-%-%-----%---%-----%-%---%','%%%%%-%-%-%%%%%%%%%-%%%%%%%%%%%-%-%%%','%---%-%-----------%-%-----%---%-%---%','%-%%%-%%%%%-%%%%%%%%%-%%%%%-%-%-%%%-%','%-%---%------%--------%-----%-------%','%-%-%-%%%%%-%%%-%-%-%-%-%%%%%%%%%%%%%','%-%-%---%-----%-%-%-%-------%---%-%-%','%-%-%%%-%%%-%-%-%-%%%%%%%%%-%%%-%-%-%','%-%---%-%---%-%-%---%-%---%-%-%-----%','%-%%%-%%%-%%%%%-%%%-%-%-%%%%%-%-%%%%%','%-------%---%-----%-%-----%---%-%---%','%%%-%-%%%%%-%%%%%-%%%-%%%-%-%%%-%-%%%','%-%-%-%-%-%-%-%-----%-%---%-%---%-%-%','%-%-%%%-%-%-%-%-%%%%%%%%%-%-%-%-%-%-%','%---%---%---%-----------------%-----%','%-%-%-%-%%%-%%%-%%%%%%%-%%%-%%%-%%%-%','%.%-%-%-------%---%-------%---%-%--P%','%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%']


def manhattan(r,c,r1,c1):
	return abs(r1 - r) + abs(c1 - c)

parent = OrderedDict()
closeSet = OrderedDict()
openSet = OrderedDict()
def astar( r, c, pacman_r, pacman_c, food_r, food_c, grid):
	openSet[(pacman_r, pacman_c)] = True

	parent[(pacman_r, pacman_c)] = None
	
	gScore = OrderedDict()
	gScore[(pacman_r, pacman_c)] = 0

	fScore = OrderedDict()
	fScore[(pacman_r, pacman_c)] = manhattan(pacman_r, pacman_c, food_r, food_c)

	while(len(openSet)!=0):
		stepX,stepY = sorted([(point,fScore[point]) for point in openSet],key=lambda x:x[1])[0][0]
		current = (stepX,stepY)
		del openSet[current]
		if grid[stepX][stepY] == ".":
			stack = []
			break
		closeSet[current] = True
		
		for (x,y) in [(-1,0),(0,-1),(0,1),(1,0)]:
			newX = stepX+x
			newY = stepY+y
			neighbor = (newX,newY)
			if (newX<=r and newY<=c and grid[newX][newY] != "%"):
				if closeSet.has_key(neighbor):
					continue
				# The distance from start to a neighbor
				tentative_gScore = gScore[current] + 1#dist_between(current, neighbor)
				if not openSet.has_key(neighbor):
					openSet[neighbor] = True
				elif tentative_gScore >= gScore.get(neighbor,sys.maxint):
					continue	

				parent[neighbor] = current
				gScore[neighbor] = tentative_gScore
				fScore[neighbor] = gScore[neighbor] + manhattan(newX,newY,food_r, food_c)


astar( r, c, pacman_r, pacman_c, food_r, food_c, grid)
# print len(explored)
# print "\n".join(["%d %d"%(x,y) for x,y in explored])

path = OrderedDict()

curr = parent[(food_r, food_c)]
path[(food_r, food_c)] = True
path[curr] = True
while(not curr == None):
	path[curr] = True
	curr = parent[curr]


print len(path)-1
print "\n".join(["%d %d"%(x,y) for x,y in path ][::-1])

# for x,line in enumerate(grid):
# 	print "".join([ chart for y,chart in enumerate(line)])
# print ""
# for x,line in enumerate(grid):
# 	print "".join([ "*" if path.has_key((x,y)) else chart for y,chart in enumerate(line)])

