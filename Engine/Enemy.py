from copy import copy
from datetime import datetime
from threading import Event, Thread
import threading
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
		self.lock.acquire()
		try:
			self.x += dx
			self.y += dy
		finally:
			self.lock.release()
	
	def __init__(self, quitEvent: Event, x=0, y=0, health=2):
		super().__init__()
		self.lock = threading.Lock()
		self.x, self.y = x, y
		self.health = health
		self.path = Path(400, 600)
		self.quitEvent = quitEvent

	def run(self):
		last_move = datetime.now()
		while self.health > 0 and not self.quitEvent.is_set():
			current_move = datetime.now()
			delta_time = (current_move - last_move).microseconds
			self.move(*self.path.getMove((self.x, self.y), delta_time))
			time.sleep(0.1)
	def hit(self, damage: int) -> None:
		self.lock.acquire()
		try:
			self.health-= damage
		finally:
			self.lock.release()