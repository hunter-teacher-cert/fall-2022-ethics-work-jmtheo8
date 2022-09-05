
def getStones(currentStones):
	global stones
	
	print("How many stone(s) will you take from the pile? ", end='')
	take = int(input())
	
	if (take < 1 or take > 3):
		print("ERROR...Number of stones must be between 1 and 3. Try again.\n")
		getStones(currentStones)
		return
	
	stones = currentStones - take
	print(f'You took {take} stone(s).')
	print(f'{stones} stones remaining.\n')

def compTurn(currentStones):
	global stones
	
	take = currentStones % 4
	stones = currentStones - take
	print (f'Computer takes {take} stones.')
	print (f'{stones} stones remain.\n')
	

stones = 21
while (stones > 0):
	getStones(stones)
	compTurn(stones)

print("The computer won!")
print("Try again?")