from threading import Event, Thread
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
	
	def __init__(self, quitEvent: Event, x=0, y=0, health=0):
		super().__init__()
		self.x, self.y = x, y
		self.health = 2
		self.path = Path(400, 600)
		self.quitEvent = quitEvent

	def run(self):
		last_move = time.time()
		while self.health > 0 and self.x != 400 and self.y != 600 and not self.quitEvent.is_set():
			current_move = time.time()
			delta_time = current_move - last_move
			self.move(*self.path.getMove((self.x, self.y), delta_time))
			
	def hit(self, damage: int) -> None:
		self.health -= damage