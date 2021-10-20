from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()
canvas.drawOval(100, 240, 175, 150)
canvas.drawOval(125, 140, 125, 100)
canvas.drawOval(138, 70, 96, 71)
canvas.drawLine(350, 300, 250, 180)
canvas.drawLine(30, 300, 125, 180)


win.wait()
