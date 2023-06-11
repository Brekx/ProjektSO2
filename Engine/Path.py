from math import sqrt
from typing import Tuple

class Path:
	end: Tuple[int, int]
	speed: int

	def __init__(self, x=800, y=600, speed=.01) -> None:
		self.end = (x, y)
		self.speed = speed

	def getMove(self, position, T: int):
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