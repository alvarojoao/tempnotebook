#!/usr/bin/python
from collections import OrderedDict
 
pacman_r = 11
pacman_c = 9
food_r = 2
food_c = 15
r = 13 
c = 20
grid = ['%%%%%%%%%%%%%%%%%%%%','%----%--------%----%','%-%%-%-%%--%%-%.%%-%','%-%-----%--%-----%-%','%-%-%%-%%--%%-%%-%-%','%-----------%-%----%','%-%----%%%%%%-%--%-%','%-%----%----%-%--%-%','%-%----%-%%%%-%--%-%','%-%-----------%--%-%','%-%%-%-%%%%%%-%-%%-%','%----%---P----%----%','%%%%%%%%%%%%%%%%%%%%']
marked = OrderedDict()
explored = OrderedDict()
parent = OrderedDict()
path = OrderedDict()

def dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid):
	stack = [(pacman_r, pacman_c)]
	marked[(pacman_r,pacman_c)] = True
	parent[(pacman_r, pacman_c)] = None
	while(len(stack)!=0):
		stepX,stepY = stack.pop()
		explored[(stepX,stepY)] = True
		if grid[stepX][stepY] == ".":
			stack = []
			break
		for (x,y) in [(-1,0),(0,-1),(0,1),(1,0)]:
			newX = stepX+x
			newY = stepY+y
			if (newX<=r and newY<=c and grid[newX][newY] != "%"):
				if not marked.has_key((newX,newY)):
					stack.append((newX,newY))
					marked[(newX,newY)] = True
					parent[(newX,newY)] = (stepX,stepY)

dfs( r, c, pacman_r, pacman_c, food_r, food_c, grid)
print len(explored)
print "\n".join(["%d %d"%(x,y) for x,y in explored])

curr = parent[(food_r, food_c)]
path[(food_r, food_c)] = True
path[curr] = True
while(not curr == None):
	path[curr] = True
	curr = parent[curr]


print len(path)
print "\n".join(["%d %d"%(x,y) for x,y in path ][::-1])

# for x,line in enumerate(grid):
# 	print "".join([ chart for y,chart in enumerate(line)])
# print ""
# for x,line in enumerate(grid):
# 	print "".join([ "*" if path.has_key((x,y)) else chart for y,chart in enumerate(line)])

