from threading import Thread
import time
from Engine.Path import Path

class Enemy(Thread):
	x: int
	y: int
	health: int
	path: Path

	def getPosition(self):
		return (self.x, self.y)
	
	def move(self, dx: int, dy: int):
		self.x += dx
		self.y += dy
	
	def __init__(self):
		super().__init__()
		# super().__init__('Mammal')
		self.x, self.y = 0, 0
		self.health = 2
		self.path = Path()

	def run(self):
		last_move = time.time()
		while self.health > 0: # not at the end
			current_move = time.time()
			delta_time = current_move - last_move
			self.move(*self.path.getMove((self.x, self.y), delta_time))
			time.sleep(.1)
			self.health -= 1
