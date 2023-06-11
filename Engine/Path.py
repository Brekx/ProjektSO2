from math import sqrt
from typing import Tuple

class Path:
	end: Tuple[int, int]
	speed: int

	def __init__(self, x=800, y=600, speed=.01) -> None:
		"""Path(x, y)
		Args:
			x: int target x
			y: int target y
			speed: int speed for path follower
		"""
		self.end = (x, y)
		self.speed = speed

	def getMove(self, position, T: int):
		"""getMove(position, T: int)
		Args:
			position: (x, y) current position
			T:int passed time
		"""
		dx = self.end[0] - position[0]
		dy = self.end[1] - position[1]
		p = (dx**2 + dy**2)
		if p == 0:
			return 0, 0
		my = sqrt((dy**2 * self.speed**2) / p) * T/1000
		mx = (dx*my)/dy
		if(mx > dx and my > dy):
			return dx, dy
		return mx, my