def createMatriz(self,x,y):
	p = [1,0,1,1,1]
        matriz = []
        bricks = []
        for i in range(y):
		array = []
		for j in range(x):
			if (j+1) %2 == 0 and (i+1) %2 == 0 :
				array.append('@')
			elif not (j,i) in self.removeOnMatiz and random.choice(p):
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
                	x = random.choice(bricks)
                	bricks.remove(x)
                	y = random.choice(bricks)
                	bricks.remove(y)
                	matriz[x[0]][x[1]] = '+'
                	matriz[y[0]][y[1]] = '-'
        except:
		pass
        return matriz