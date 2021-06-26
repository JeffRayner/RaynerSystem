import random

x, y = 6,5
removeOnMatiz =  (
	(x-x,y-y), (x-x+1,y-y),(x-1,y-y), (x-2,y-y),
	(x-x,y-y+1),(x-1,y-y+1),(x-1,y-2),(x-x+1,y-1),
	(x-1,y-1), (x-2,y-1),(x-x,y-1), (x-x,y-2),
	)

def createMatriz(x,y):
	p = [1,0,1,1,1]
	matriz = []
	bricks = []
	for i in range(y):
		array = []
		for j in range(x):
			if (j+1) %2 == 0 and (i+1) %2 == 0 :
				array.append('@')
			elif not (j,i) in removeOnMatiz and random.choice(p):
				array.append('*')
				bricks.append((i+1,j+1))
			else:
				array.append(' ')
                    
		array.insert(0,'#')
		array.append('#')
		matriz.append(array)
            
	matriz.insert(0, ['#' for i in range(x+2)] )
	matriz.append( ['#' for i in range(x+2)] )
    
	try:
		for i in range(int(x/2)):
			bricks.sort()
			a = random.choice(bricks)
			bricks.remove(x)
			b = random.choice(bricks)
			bricks.remove(y)
			matriz[a[0]][b[1]] = '+'
			matriz[b[0]][b[1]] = '-'
	except:
		pass

	return matriz