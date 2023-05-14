import sys
from threading import Event, Thread
import threading
import time
from Engine.Enemy import Enemy
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QRect

from Engine.Tower import Tower
from random import Random

class MainWindow(QtWidgets.QMainWindow):
		
	def __init__(self):
		super().__init__()

		self.label = QtWidgets.QLabel()
		canvas = QtGui.QPixmap(800, 600)
		canvas.fill(Qt.white)
		self.label.setPixmap(canvas)
		self.setCentralWidget(self.label)
		self.main_thread = MainThread(self.draw)
		self.main_thread.start()

	def drawEnemy(self, x, y):
		painter = QtGui.QPainter(self.label.pixmap())
		painter.fillRect(QRect(0, 0, 800, 600), QtGui.QColor("000"))
		painter.drawImage(QRect(x, y, 50, 50), QtGui.QImage("resources/BasicEnemy.png"))
		painter.end()
		self.update()

	def draw(self, enemies_positions, towers_positions):
		painter = QtGui.QPainter(self.label.pixmap())
		painter.fillRect(QRect(0, 0, 800, 600), QtGui.QColor("000"))
		[painter.drawImage(QRect(x, y, 50, 50), QtGui.QImage("resources/BasicEnemy.png")) for x, y in enemies_positions] 
		[painter.drawImage(QRect(x, y, 50, 50), QtGui.QImage("resources/Tower.jpg")) for x, y in towers_positions] 
		painter.end()
		self.update()


class MainThread(Thread):
	# enemies: list(Enemy)
	# towers: list(Tower)

	def __init__(self, paiter):
		super().__init__()
		self.r = Random()
		self.painter = paiter

	def run(self):
		quitEvent = Event()
		self.enemies = [Enemy(quitEvent, self.r.randint(0,800), self.r.randint(0, 600)) for _ in range(20)]
		[ e.start() for e in self.enemies ]
		self.towers = [Tower(quitEvent, 50, 1, 5, (400, 500), self.enemies)]
		[ t.start() for t in self.towers ]

		
		while not quitEvent.is_set():
			self.enemies = [ e for e in self.enemies if e.is_alive() ]
			if not self.enemies:
				quitEvent.set()
			else:
				for e in self.enemies:
					x, y = e.getPosition()
					# print("Alive", x, y, threading.active_count())
			self.painter([(e.getPosition()[0], e.getPosition()[1]) for e in self.enemies], [(t.getPosition()[0], t.getPosition()[1]) for t in self.towers])
			time.sleep(.01)
		print("Dead")


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()