from math import sqrt

class Path:
	# end: tuple(int,` int)
	# speed: int`

	def __init__(self) -> None:
		self.end = (100, 100)
		self.speed = 1

	def getMove(self, position, T: int):
		dx = self.end[0] - position[0]
		dy = self.end[1] - position[1]
		p = (dx^2 + dy^2)
		if p == 0:
			return 0, 0
		my = sqrt((dy^2 * self.speed^2) / p)
		mx = (dx*my)/dy

		return mx, my