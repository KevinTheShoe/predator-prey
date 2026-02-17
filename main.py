import random

class World:
	def __init__(self, width, height):
		self.currentID = 0
		self.predators = [Predator(self.genID(), width - 1, height - 1)]
		self.prey = [Prey(self.genID(), 0, 0)]
		self.width = width
		self.height = height
	
	def genID(self):
		self.currentID += 1
		return self.currentID
	
	def update(self):
		for i in range(len(self.predators)):
			self.predators[i].move(self)
			self.predators[i].eat(self)
		for i in range(len(self.prey)):
			self.prey[i].move(self)
			self.prey[i].reproduce(self)
	
	def draw(self):
		map = [['.' for i in range(self.width)] for i in range(self.height)]
		# plot the things
		for p in self.prey:
			map[p.y][p.x] = 'R'
		for p in self.predators:
			map[p.y][p.x] = 'W'

		for row in map:
			for col in row:
				print(col, end='')
			print()

class Prey:
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y

	def move(self, world):
		match random.randint(1, 5):
			case 1: self.x += 1
			case 2: self.x -= 1
			case 3: self.y += 1
			case 4: self.y -= 1
			case 5: pass
		
		if self.x >= world.width: self.x = world.width - 1
		if self.y >= world.height: self.y = world.height - 1
		if self.x < 0: self.x = 0
		if self.y < 0: self.y = 0
	
	def reproduce(self, world):
		if random.randint(1, 20) == 1: world.prey.append(Prey(world.genID, self.x, self.y))

class Predator:
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y

	def move(self, world):
		match random.randint(1, 5):
			case 1: self.x += 1
			case 2: self.x -= 1
			case 3: self.y += 1
			case 4: self.y -= 1
			case 5: pass
		
		if self.x >= world.width: self.x = world.width - 1
		if self.y >= world.height: self.y = world.height - 1
		if self.x < 0: self.x = 0
		if self.y < 0: self.y = 0
	
	def eat(self, world):
		newPrey = []
		for p in world.prey:
			if not (p.x == self.x and p.y == self.y): newPrey.append(p)
		world.prey = newPrey

if __name__ == '__main__':
	world = World(10, 10)
	while True:
		world.draw()
		world.update()
		d = input()