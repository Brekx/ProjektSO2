from threading import Thread
import time
from Engine.Enemy import Enemy

class MainThread(Thread):
	def run(self):
		a = Enemy()
		a.start()
		while a.is_alive():
			print("Alive", a.getPosition())
			a.move(-50, 0)
			time.sleep(.1)
			
		print("Dead")

if __name__ == "__main__":
	main = MainThread()
	main.start()