from threading import Event, Thread
from typing import Tuple


class Tower(Thread):
	range: int
	damage: int
	reload: int
	quitEvent: Event
	position: Tuple[int, int]

	def __init__(self, quitEvent, range, damage, reload, position, enemies) -> None:
		super().__init__()
		self.range = range**2
		self.damage = damage
		self.reload = reload
		self.position = position
		self.enemies = enemies
		self.quitEvent = quitEvent

	def run(self):
		while not self.quitEvent.is_set():
			for e in self.enemies:
				x, y = e.getPosition()
				if (self.position[0]-x)**2 + (self.position[1]-y)**2 <= self.range:
					e.hit(self.damage)
	def getPosition(self):
		return self.position