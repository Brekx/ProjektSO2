from datetime import datetime
import sys
from threading import Event, Thread
import time
from typing import List
from Engine.Enemy import Enemy
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QRect

from Engine.Tower import Tower
from random import Random

class MainWindow(QtWidgets.QMainWindow):
	pressPos = None
		
	def __init__(self):
		super().__init__()

		self.label = QtWidgets.QLabel()
		canvas = QtGui.QPixmap(800, 600)
		canvas.fill(Qt.white)
		self.label.setPixmap(canvas)
		self.setCentralWidget(self.label)
		self.main_thread = MainThread(self.draw)
		self.main_thread.start()

	def draw(self, enemies_positions, towers_positions, available_towers):
		painter = QtGui.QPainter(self.label.pixmap())
		painter.fillRect(QRect(0, 0, 800, 600), QtGui.QColor(0, 0, 0))
		painter.drawImage(QRect(350, 500, 100, 100), QtGui.QImage("resources/Castle.png"))
		[painter.drawImage(QRect(x, y, 50, 50), QtGui.QImage("resources/BasicEnemy.png")) for x, y in enemies_positions] 
		[painter.drawImage(QRect(x, y, 50, 72), QtGui.QImage("resources/Tower.png")) for x, y in towers_positions]
		painter.setPen(QtGui.QColor(255, 255, 255))
		painter.drawText(50, 50, 150, 50, 0, "Available towers: "+str(available_towers))
		painter.end()
		self.update()

	def mousePressEvent(self, event):
			if event.button() == Qt.LeftButton:
					self.pressPos = event.pos()

	def mouseReleaseEvent(self, event):
			if (self.pressPos is not None and 
					event.button() == Qt.LeftButton and 
					event.pos() in self.rect()):
							self.main_thread.addTower(event.pos().x(), event.pos().y())
			self.pressPos = None


class MainThread(Thread):
	enemies: List[Enemy]
	towers: List[Tower]
	available_towers: int

	def __init__(self, paiter):
		super().__init__()
		self.r = Random()
		self.painter = paiter
		self.quitEvent = None
		self.available_towers = 1

	def addTower(self, x, y):
		if self.available_towers > 0:
			self.towers.append(Tower(self.quitEvent, 100, 1, 5, (x, y)))

	def run(self):
		self.quitEvent = Event()
		self.enemies = []
		self.towers = []
		start = datetime.now()
		
		while not self.quitEvent.is_set():
			self.enemies = [ e for e in self.enemies if e.is_alive() ]
			self.painter([(e.getPosition()[0], e.getPosition()[1]) for e in self.enemies], [(t.getPosition()[0], t.getPosition()[1]) for t in self.towers], ((datetime.now()-start).seconds//10+1)-len(self.towers))
			self.available_towers = ((datetime.now()-start).seconds//10+1)-len(self.towers)
			for _ in range(((datetime.now()-start).seconds//5+1)-len(self.enemies)):
				self.enemies.append(Enemy(self.quitEvent, self.r.randint(0,800), self.r.randint(0, 200)))
				self.enemies[-1].start()
			for t in self.towers:
				t.deal_damage(self.enemies)
			if len(["hit" for e in self.enemies if e.x == 400 and e.y == 600])>0:
				self.quitEvent.set()
			time.sleep(.01)
		print("End")


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.show()
	app.exec_()