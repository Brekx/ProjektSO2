from Engine.Enemy import Enemy

a = Enemy()
a.start()
while a.is_alive():
  print("Alive")
print("Dead")
