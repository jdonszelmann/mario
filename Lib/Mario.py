import pyglet
from pyglet.window.key import *
from .vector import Vector

window = ...
update = ...
keys = ...

def init(win,upd,kb):
	global window, update, keys
	window = win
	update = upd
	keys = kb
	mario = Mario()

class statehandler:
	class _Statehandler:
		def __init__(self,item,state):
			self.properties = state
			self.item = item

	def __init__(self):
		self.states = []

	def __setitem__(self,key,item):
		s = self._Statehandler(key,item)
		self.states.append(s)

	def search(self,**kwargs):
		possibilities = self.states
		for i in self.states:
			for key,item in kwargs.items():
				if i.properties[key] != item and i in possibilities:
					possibilities.remove(i)
		return possibilities
		


class Mario:
	def __init__(self):
		assert window

		self.x = Vector(0,0)
		self.v = Vector(0,0)
		self.a = Vector(0,0)

		self.pus = 0
		self.sub = False
		self.state = "standing"
		self.part = 0

		self.textures = statehandler()
		self.textures[{"state":"standing","pus":0,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario.bmp")
		self.textures[{"state":"standing","pus":1,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario1.bmp")
		self.textures[{"state":"standing","pus":2,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario2.bmp")
		self.textures[{"state":"standing","pus":0,"sub":True,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario_s0.bmp")
		self.textures[{"state":"standing","pus":1,"sub":True,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario_s1.bmp")
		self.textures[{"state":"standing","pus":2,"sub":True,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario2s.bmp")

		self.textures[{"state":"end","pus":0,"sub":False,"part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario_end.bmp")
		self.textures[{"state":"end","pus":0,"sub":False,"part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario_end1.bmp")
		self.textures[{"state":"end","pus":1,"sub":False,"part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario1_end.bmp")
		self.textures[{"state":"end","pus":1,"sub":False,"part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario1_end1.bmp")
		self.textures[{"state":"end","pus":2,"sub":False,"part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario2_end.bmp")
		self.textures[{"state":"end","pus":2,"sub":False,"part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario2_end1.bmp")
		self.textures[{"state":"end","pus":0,"sub":True,"part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario_s0_end.bmp")
		self.textures[{"state":"end","pus":0,"sub":True,"part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario_s0_end1.bmp")
		self.textures[{"state":"end","pus":1,"sub":True,"part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario_s1_end.bmp")
		self.textures[{"state":"end","pus":1,"sub":True,"part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario_s1_end1.bmp")
		self.textures[{"state":"end","pus":2,"sub":True,"part":0,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario2s_end.bmp")
		self.textures[{"state":"end","pus":2,"sub":True,"part":1,"parts":2}] = pyglet.image.load("./Lib/data/textures/mario/mario2s_end1.bmp")

		self.textures[{"state":"jump","pus":0,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario_jump.bmp")
		self.textures[{"state":"jump","pus":1,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario1_jump.bmp")
		self.textures[{"state":"jump","pus":2,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario2_jump.bmp")
		self.textures[{"state":"jump","pus":0,"sub":True,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario_s0_jump.bmp")
		self.textures[{"state":"jump","pus":1,"sub":True,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario_s1_jump.bmp")
		self.textures[{"state":"jump","pus":2,"sub":True,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario2s_jump.bmp")



		self.sprite = pyglet.sprite.Sprite(self.textures[{"state":self.state,"pus":self.pus,"sub":self.sub,"part":self.part}],self.x.x,self.x.y, usage='dynamic', subpixel=False)

		update.register(self)

	def ApplyForce(self,x,y=0):
		if type(x) == Vector:
			self.a = x
		else:
			self.a = Vector(x,y)

	def update(self):
		if keys[W]:
			self.ApplyForce(0,1)
		elif keys[A]:
			self.ApplyForce(-1,0)
		elif keys[S]:
			pass
		elif keys[D]:
			self.ApplyForce(1,0)

		self.v += self.a
		self.x += self.v
		self.v *= Vector(0.6,0.6)
		self.a = Vector(0,0)
		self.sprite.set_position(self.x.x, self.x.y)

	def draw(self):
		self.sprite.draw()