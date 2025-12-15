import TomFunctions as t

t.move(-110,0)
for i in range(20):
  t.tree(random.randint(7,12),3)
  t.move(-150+(i*40),0)
