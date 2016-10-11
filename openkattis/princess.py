n=5
r,c = (1,3)
grid = ['-----',
        '---m-',
        '-----',
        '-p---',
        '-----']

def moveStr(i):
	if i==0:
		return "UP"
	if i==1:
		return "LEFT"
	if i==2:
		return "RIGHT"
	if i==3:
		return "DOWN"

def reversedMoveStr(move):
    if move=="UP":
        return "DOWN"
    if move=="LEFT":
        return "RIGHT"
    if move=="RIGHT":
        return "LEFT"
    if move=="DOWN":
        return "UP"
m_start = (r,c)
parent = {}

def searchPath(grid,m_start):
    marked = {}
    marked[str(m_start)] = True
    stack = [m_start]
    m_start = (r,c)
    parent[m_start]=(None,None)
    while(len(stack)!=0):
        atual = stack.pop(0)
        x,y = atual
        current = (x,y)
        if grid[x][y] == 'p':
            return (x,y)
        for i,(xx,yy) in enumerate([(-1,0),(0,-1),(0,1),(1,0)]):
            newX = x+xx
            newY = y+yy
            nextP = (newX,newY)
            if newX >=0 and newX<n and newY >=0 and newY <n:
                if not marked.has_key(str(nextP)):
                    marked[str(nextP)] = True
                    stack.append(nextP)
                    parent[nextP]=(current,moveStr(i))

princess = searchPath(grid,m_start)

path = []
curr = parent[princess]
while(not curr[0] == None):
    path.append((curr[1]))
    curr =  parent[curr[0]]
# print "\n".join(path)
print path[0]

