from threading import Event, Thread
import time
from typing import Tuple


class Tower():
	range: int
	damage: int
	reload: int
	quitEvent: Event
	position: Tuple[int, int]

	def __init__(self, quitEvent, range, damage, reload, position) -> None:
		"""Tower(quitEvent, range, damage, reload, position)
		Args:
			quitEvent: handle to quit event
			range: int range of the tower
			damage: int damage dealt to enemy
			reload: int time to reload
			position: (x, y) position of the tower
		"""
		super().__init__()
		self.range = range**2
		self.damage = damage
		self.reload = reload
		self.position = position
		self.quitEvent = quitEvent

	def deal_damage(self, enemies):
		"""deal_damage(enemies)
			calculates damage dealt to enemies
		Args:
			enemies: List(Enemy) 
		"""
		for e in enemies:
			x, y = e.getPosition()
			if ((self.position[0]+25)-x)**2 + ((self.position[1]+25)-y)**2 <= self.range:
				e.hit(5)

	def getPosition(self):
		"""getPosition()
		Returns:
			position: (x, y)
		"""
		return self.position