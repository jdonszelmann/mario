import pyglet, copy
from pyglet.window.key import *
from pyglet.gl import *
from .vector import Vector

window = ...
update = ...
keys = ...
world = ...

def init(win,upd,kb,wrld):
	global window, update, keys, world
	window = win
	update = upd
	keys = kb
	world = wrld
	mario = Mario()

class statehandler:
	class _Statehandler:
		def __init__(self,state,item):
			self.properties = state
			self.item = item

	def __init__(self):
		self.states = []

	def __setitem__(self,key,item):
		s = self._Statehandler(key,item)
		self.states.append(s)

	def __getitem__(self,thing):
		possibilities = copy.copy(self.states)
		for i in self.states:
			for key,item in thing.items():
				if i.properties[key] != item and i in possibilities:
					possibilities.remove(i)
		return possibilities
		


class Mario:
	def __init__(self):
		assert window

		self.x = Vector(0,100)
		self.v = Vector(0,0)

		self.pus = 2
		self.sub = False
		self.state = "standing"
		self.part = 0
		self.parts = 0
		self.flipped = True
		self.partcounter = 0
		self.in_jump = False

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

		self.textures[{"state":"move","pus":0,"sub":False,"part":0,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_move0.bmp")
		self.textures[{"state":"move","pus":0,"sub":False,"part":1,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_move1.bmp")
		self.textures[{"state":"move","pus":0,"sub":False,"part":2,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_move2.bmp")
		self.textures[{"state":"move","pus":1,"sub":False,"part":0,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario1_move0.bmp")
		self.textures[{"state":"move","pus":1,"sub":False,"part":1,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario1_move1.bmp")
		self.textures[{"state":"move","pus":1,"sub":False,"part":2,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario1_move2.bmp")
		self.textures[{"state":"move","pus":2,"sub":False,"part":0,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario2_move0.bmp")
		self.textures[{"state":"move","pus":2,"sub":False,"part":1,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario2_move1.bmp")
		self.textures[{"state":"move","pus":2,"sub":False,"part":2,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario2_move2.bmp")
		self.textures[{"state":"move","pus":0,"sub":True,"part":0,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_s0_move0.bmp")
		self.textures[{"state":"move","pus":0,"sub":True,"part":1,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_s0_move1.bmp")
		self.textures[{"state":"move","pus":0,"sub":True,"part":2,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_s0_move2.bmp")
		self.textures[{"state":"move","pus":1,"sub":True,"part":0,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_s1_move0.bmp")
		self.textures[{"state":"move","pus":1,"sub":True,"part":1,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_s1_move1.bmp")
		self.textures[{"state":"move","pus":1,"sub":True,"part":2,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario_s1_move2.bmp")
		self.textures[{"state":"move","pus":2,"sub":True,"part":0,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario2s_move0.bmp")
		self.textures[{"state":"move","pus":2,"sub":True,"part":1,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario2s_move1.bmp")
		self.textures[{"state":"move","pus":2,"sub":True,"part":2,"parts":3}] = pyglet.image.load("./Lib/data/textures/mario/mario2s_move2.bmp")

		self.textures[{"state":"squat","pus":1,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario1_squat.bmp")
		self.textures[{"state":"squat","pus":2,"sub":False,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario2_squat.bmp")
		self.textures[{"state":"squat","pus":2,"sub":True,"part":0,"parts":1}] = pyglet.image.load("./Lib/data/textures/mario/mario2s_squat.bmp")

		self.sprite = pyglet.sprite.Sprite(self.get_texture(),self.x.x,self.x.y, usage='dynamic', subpixel=False)

		update.register(self)


	def get_texture(self):
		t = self.textures[{"state":self.state,"pus":self.pus,"sub":self.sub}]
		if self.parts != t[0].properties["parts"]:
			self.parts = t[0].properties["parts"]
			self.part = 0
		t = self.textures[{"state":self.state,"pus":self.pus,"sub":self.sub,"part":self.part}]
		assert len(t) == 1
		return t[0].item

	def update(self, dt):
		maxxv = 300
		changed = False

		self.partcounter += 1
		if self.partcounter > 10:
			self.partcounter = 0
			self.part += 1

		if self.part >= self.parts:
			self.part = 0

		if keys[W] and not self.in_jump:
			self.v.y = 500
			self.in_jump = True
		if keys[A]:
			if self.v.x > 0:
				self.v.x -= 25
			else:
				self.v.x -= 10
		if keys[S]:
			if self.pus > 0 and not (self.pus == 1 and self.sub):
				if self.v.x > 20:
					self.v.x -= 20
				elif self.v.x < -20:
					self.v.x += 20
				else:
					self.v.x = 0		
				self.state = "squat"
				changed = True
		if keys[D]:
			if self.v.x < 0:
				self.v.x += 25
			else:
				self.v.x += 10
	
		if self.in_jump:
			self.v.y -= 15

		if self.x.y + (self.v.y * dt) <= 0:
			while True:
				if self.v.y > 90:
					self.v.y -= 90
				elif self.v.y < -90:
					self.v.y += 90
				elif not (self.x.y + (self.v.y * dt) <= 0):
					break
				else:
					self.in_jump = False
					self.v.y = 0
					break
		
		if self.x.x + (self.v.x * dt) <= 0:
			while True:
				if self.v.x > 90:
					self.v.x -= 90
				elif self.v.x < -90:
					self.v.x += 90
				elif not (self.x.x + (self.v.x * dt) <= 0):
					break
				else:
					self.v.x = 0
					break
		
		
		if self.x.x + (self.v.x * dt) >= world.width - self.sprite.width:
			while True:
				if self.v.x > 90:
					self.v.x -= 90
				elif self.v.x < -90:
					self.v.x += 90
				elif not (self.x.x + (self.v.x * dt) >= world.width - self.sprite.width):
					break
				else:
					self.v.x = 0
					break
		x,y = world.check_colision(self.x.x + (self.v.x * dt),self.x.y,self.sprite.width,self.sprite.height,"<")
		if x != None and self.x.x + (self.v.x * dt) > x:
			while True:
				if self.v.x > 90:
					self.v.x -= 90
				elif self.v.x < -90:
					self.v.x += 90
				elif not (self.x.x + (self.v.x * dt) > x):
					break
				else:
					self.v.x = 0
					break	

		x,y = world.check_colision(self.x.x + (self.v.x * dt),self.x.y,self.sprite.width,self.sprite.height,">")
		if x != None and self.x.x + self.sprite.width + (self.v.x * dt) > x:
			while True:
				if self.v.x > 90:
					self.v.x -= 90
				elif self.v.x < -90:
					self.v.x += 90
				elif not (self.x.x + self.sprite.width + (self.v.x * dt) > x):
					break
				else:
					self.v.x = 0
					break			

		x,y = world.check_colision(self.x.x + (self.v.x * dt),self.x.y,self.sprite.width,self.sprite.height,"v")
		if x != None and self.x.y + (self.v.y * dt) <= y:
			while True:
				if self.v.y > 90:
					self.v.y -= 90
				elif self.v.y < -90:
					self.v.y += 90
				elif not (self.x.y + (self.v.y * dt) <= y):
					break
				else:
					self.in_jump = False
					self.v.y = 0
					break		

		x,y = world.check_colision(self.x.x + (self.v.x * dt),self.x.y,self.sprite.width,self.sprite.height,"^")
		if x != None and self.x.y + self.sprite.height + (self.v.y * dt) > y:
			while True:
				if self.v.y > 50:
					self.v.y -= 50
				elif self.v.y < -50:
					self.v.y += 50
				elif not (self.x.y + self.sprite.height > y):
					break
				else:
					self.v.y = 0
					break	

		x,y = world.check_colision(self.x.x,self.x.y + (self.v.y * dt),self.sprite.width,self.sprite.height,"v")
		if x != None and self.x.y + (self.v.y * dt) <= y:
			while True:
				if self.v.y > 90:
					self.v.y -= 90
				elif self.v.y < -90:
					self.v.y += 90
				elif not (self.x.y + (self.v.y * dt) <= y):
					break
				else:
					self.in_jump = False
					self.v.y = 0
					break		

		x,y = world.check_colision(self.x.x,self.x.y + (self.v.y * dt),self.sprite.width,self.sprite.height,"^")
		if x != None and self.x.y + self.sprite.height + (self.v.y * dt) > y:
			while True:
				if self.v.y > 50:
					self.v.y -= 50
				elif self.v.y < -50:
					self.v.y += 50
				elif not (self.x.y + self.sprite.height > y):
					break
				else:
					self.v.y = 0
					break	
	

		x,y = world.check_colision(self.x.x,self.x.y + (self.v.y * dt),self.sprite.width,self.sprite.height,"<")
		if x != None and self.x.x + (self.v.x * dt) > x:
			while True:
				if self.v.x > 90:
					self.v.x -= 90
				elif self.v.x < -90:
					self.v.x += 90
				elif not (self.x.x + (self.v.x * dt) > x):
					break
				else:
					self.v.x = 0
					break	

		x,y = world.check_colision(self.x.x,self.x.y + (self.v.y * dt),self.sprite.width,self.sprite.height,">")
		if x != None and self.x.x + self.sprite.width + (self.v.x * dt) > x:
			while True:
				if self.v.x > 90:
					self.v.x -= 90
				elif self.v.x < -90:
					self.v.x += 90
				elif not (self.x.x + self.sprite.width + (self.v.x * dt) > x):
					break
				else:
					self.v.x = 0
					break			



		if world.overlap(self.x.x,self.x.y-1,self.sprite.width,self.sprite.height) == 0 and not self.in_jump:
			self.in_jump = True			

		if not (keys[A] or keys[D]):
			if self.v.x > 10:
				self.v.x -= 10
			elif self.v.x < -10:
				self.v.x += 10
			else:
				self.v.x = 0

		self.v.x = maxxv if self.v.x > maxxv else self.v.x
		self.v.x = -maxxv if self.v.x < -maxxv else self.v.x
		self.x += self.v.mult(dt)

		self.sprite.set_position(self.x.x, self.x.y)

		if abs(self.v.x) > 0.5 and not self.in_jump and not self.state == "squat":
			self.state = "move"
			changed = True
		if self.in_jump:
			self.state = "jump"
			changed = True
		if self.v.x < -0.2:
			self.flipped = True
		elif self.v.x > 0.2:
			self.flipped = False

		if not changed:
			self.state = "standing"
		
		scrollX = window.width/2 - self.sprite.width/2 - self.x.x
		scrollY = window.height/2 - self.sprite.height/2 - self.x.y

		if self.x.x < window.width/2 - self.sprite.width/2:
			scrollX = 0
		if self.x.x > world.width - window.width/2 - self.sprite.width/2:
			scrollX = -(world.width - window.width)
		if self.x.y >= window.height/2 - self.sprite.height/2:
			scrollY = 0
		if self.x.y < -world.height + window.height + window.height/2 - self.sprite.height/2:
			scrollY = world.height - window.height	

		world.scroll_x = scrollX
		world.scroll_y = scrollY

		t = self.get_texture()
		t.anchor_x = 0
		if self.flipped:
			t.anchor_x = t.width//2
			t = t.get_texture().get_transform(flip_x = True)
			t.anchor_x = 0		
		self.sprite.image = t

	def draw(self):
		self.sprite.draw()