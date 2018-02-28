import pyglet
from . import Enemy



class goomba_brown(Enemy.Enemy):
	def __init__(self,x,y):
		super().__init__(x,y)

		self.textures[{"state":"move","part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/goombas_0.bmp")
		self.textures[{"state":"move","part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/goombas_1.bmp")
		self.textures[{"state":"jump","part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/goombas_0.bmp")
		self.textures[{"state":"jump","part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/goombas_1.bmp")
		self.textures[{"state":"dead","part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/goombas_ded.bmp")
		self.textures[{"state":"standing","part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/goombas_0.bmp")
		self.textures[{"state":"standing","part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/goombas_1.bmp")

		self.direction = True
		self.maxxv = 50

		self.state = "move"
		self.post_init()

	def AI(self):
		self.keys["right"] = False
		self.keys["left"] = False

		if self.state == "standing":
			self.direction = not self.direction

		if self.direction == True:
			self.keys["right"] = True
		if self.direction == False:
			self.keys["left"] = True

