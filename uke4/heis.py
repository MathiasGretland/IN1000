from ezgraphics import GraphicsWindow
from time import sleep
vindu = GraphicsWindow()
lerret = vindu.canvas()

y = 0
while y<200:
    lerret.clear()
    lerret.drawRect(10,y,50,50)
    y += 1
    sleep(0.01)
