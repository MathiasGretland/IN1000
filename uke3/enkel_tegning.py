from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()
canvas.drawRect(20, 20, 100, 75)

win.wait()
