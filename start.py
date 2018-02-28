import pyglet, sys
from pyglet.gl import *
from Lib import Enemy,Mario,World

#setting up window
window = pyglet.window.Window(640,480,resizable=False,vsync=True,caption="Super Mario Bros")
icon1 = pyglet.image.load('./Lib/data/icons/app.ico')
window.set_icon(icon1)
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)

#background:white
glClearColor(1,1,1,1)

@window.event
def on_draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
	glEnable(GL_LINE_SMOOTH);
	glHint(GL_LINE_SMOOTH_HINT, GL_NICEST);
	glEnable(GL_BLEND);
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
	glEnable(GL_CULL_FACE);
	glCullFace(GL_BACK);
	glEnable(GL_LINE_STIPPLE)
	glShadeModel(GL_SMOOTH)
	update.draw()

@window.event
def on_close():
	window.close()
	sys.exit()


#this class makes all other screenobjects update 60x/s
class Update:
	def __init__(self):
		self.objects = []

	def __call__(self,dt):
		for i in self.objects:
			i.update(dt)

	def draw(self):
		for i in self.objects:
			i.draw()

	def register(self,obj):
		self.objects.append(obj)

update = Update()

# initialization of modules
world = World.init(window,update,keys)
Enemy.init(window,update,keys,world)
Mario.init(window,update,keys,world)


#starting eventloop
event_loop = pyglet.app.EventLoop()
pyglet.clock.schedule_interval(update, 1/60.0)
event_loop.run()








