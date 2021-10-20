from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()

canvas.drawOval(20, 20, 50, 50)
canvas.drawOval(120, 20, 50, 50)
canvas.drawOval(220, 40, 50, 50)
canvas.drawOval(320, 60, 50, 70)

win.wait()
