import pyglet
from . import worlds
from pyglet.gl import *

window = ...
update = ...
keys = ...
world = ...

def init(win,upd,kb):
	global window, update, keys, world
	window = win
	update = upd
	keys = kb
	world = World()
	return world


class World:
	def __init__(self):
		assert window
		self.scale = 32

		self.scroll_x = 0
		self.scroll_y = 0

		self.world_number = 1
		self.world_subnumber = 1
		self.background_batch = pyglet.graphics.Batch()
		self.foreground_batch = pyglet.graphics.Batch()
		self.texturedb = {
			"bush_L":pyglet.image.load("./Lib/data/textures/grass_left.bmp"),
			"bush_C":pyglet.image.load("./Lib/data/textures/grass_center.bmp"),
			"bush_R":pyglet.image.load("./Lib/data/textures/grass_right.bmp"),
			"castle_brick_0":pyglet.image.load("./Lib/data/textures/castle0_brick.bmp"),
			"castle_brick_1":pyglet.image.load("./Lib/data/textures/castle1_brick.bmp"),
			"brick_red":pyglet.image.load("./Lib/data/textures/brickred.bmp"),
			"brick_1":pyglet.image.load("./Lib/data/textures/brick1.bmp"),
			"brick_2":pyglet.image.load("./Lib/data/textures/brick2.bmp"),
			"bush_center_0":pyglet.image.load("./Lib/data/textures/bush_center_0.bmp"),
			"bush_center_1":pyglet.image.load("./Lib/data/textures/bush_center_1.bmp"),
			"bush_left":pyglet.image.load("./Lib/data/textures/bush_left.bmp"),
			"bush_right":pyglet.image.load("./Lib/data/textures/bush_right.bmp"),
			"bush_top":pyglet.image.load("./Lib/data/textures/bush_top.bmp"),
			"gnd_red_0":pyglet.image.load("./Lib/data/textures/gnd_red_1.bmp"),
			"gnd_red_1":pyglet.image.load("./Lib/data/textures/gnd_red2.bmp"),
			"gnd_black_0":pyglet.image.load("./Lib/data/textures/gnd1.bmp"),
			"gnd_black_1":pyglet.image.load("./Lib/data/textures/gnd1_2.bmp"),
			"gnd_white_0":pyglet.image.load("./Lib/data/textures/gnd2.bmp"),
			"gnd_white_1":pyglet.image.load("./Lib/data/textures/gnd2_2.bmp"),
			"gnd_gray":pyglet.image.load("./Lib/data/textures/gnd_4.bmp"),
			"gnd_green":pyglet.image.load("./Lib/data/textures/gnd_5.bmp"),
			"gnd_green":pyglet.image.load("./Lib/data/textures/gnd_5.bmp"),

			"question_block0_0":pyglet.image.load("./Lib/data/textures/blockq_0.bmp"),
			"question_block0_1":pyglet.image.load("./Lib/data/textures/blockq_1.bmp"),
			"question_block0_2":pyglet.image.load("./Lib/data/textures/blockq_2.bmp"),
			"question_block0_used":pyglet.image.load("./Lib/data/textures/blockq_used.bmp"),
			"question_block1_0":pyglet.image.load("./Lib/data/textures/blockq1_0.bmp"),
			"question_block1_1":pyglet.image.load("./Lib/data/textures/blockq1_1.bmp"),
			"question_block1_2":pyglet.image.load("./Lib/data/textures/blockq1_2.bmp"),
			"question_block1_used":pyglet.image.load("./Lib/data/textures/blockq1_used.bmp"),
			"question_block2_used":pyglet.image.load("./Lib/data/textures/blockq2_used.bmp"),
			
			"pipe_hor_bot_center":pyglet.image.load("./Lib/data/textures/pipe_hor_bot_center.bmp"),
			"pipe_hor_bot_left":pyglet.image.load("./Lib/data/textures/pipe_hor_bot_left.bmp"),
			"pipe_hor_bot_right":pyglet.image.load("./Lib/data/textures/pipe_hor_bot_right.bmp"),
			"pipe_hor_top_center":pyglet.image.load("./Lib/data/textures/pipe_hor_top_center.bmp"),
			"pipe_hor_top_left":pyglet.image.load("./Lib/data/textures/pipe_hor_top_left.bmp"),
			"pipe_hor_top_right":pyglet.image.load("./Lib/data/textures/pipe_hor_top_right.bmp"),
			"pipe_left_bot":pyglet.image.load("./Lib/data/textures/pipe_left_bot.bmp"),
			"pipe_left_top":pyglet.image.load("./Lib/data/textures/pipe_left_top.bmp"),
			"pipe_right_bot":pyglet.image.load("./Lib/data/textures/pipe_right_bot.bmp"),
			"pipe_right_top":pyglet.image.load("./Lib/data/textures/pipe_right_top.bmp"),
			"pipe1_hor_bot_center":pyglet.image.load("./Lib/data/textures/pipe1_hor_bot_center.bmp"),
			"pipe1_hor_bot_left":pyglet.image.load("./Lib/data/textures/pipe1_hor_bot_left.bmp"),
			"pipe1_hor_bot_right":pyglet.image.load("./Lib/data/textures/pipe1_hor_bot_right.bmp"),
			"pipe1_hor_top_center":pyglet.image.load("./Lib/data/textures/pipe1_hor_top_center.bmp"),
			"pipe1_hor_top_left":pyglet.image.load("./Lib/data/textures/pipe1_hor_top_left.bmp"),
			"pipe1_hor_top_right":pyglet.image.load("./Lib/data/textures/pipe1_hor_top_right.bmp"),
			"pipe1_left_bot":pyglet.image.load("./Lib/data/textures/pipe1_left_bot.bmp"),
			"pipe1_left_top":pyglet.image.load("./Lib/data/textures/pipe1_left_top.bmp"),
			"pipe1_right_bot":pyglet.image.load("./Lib/data/textures/pipe1_right_bot.bmp"),
			"pipe1_right_top":pyglet.image.load("./Lib/data/textures/pipe1_right_top.bmp"),
			"pipe2_hor_bot_center":pyglet.image.load("./Lib/data/textures/pipe2_hor_bot_center.bmp"),
			"pipe2_hor_bot_left":pyglet.image.load("./Lib/data/textures/pipe2_hor_bot_left.bmp"),
			"pipe2_hor_bot_right":pyglet.image.load("./Lib/data/textures/pipe2_hor_bot_right.bmp"),
			"pipe2_hor_top_center":pyglet.image.load("./Lib/data/textures/pipe2_hor_top_center.bmp"),
			"pipe2_hor_top_left":pyglet.image.load("./Lib/data/textures/pipe2_hor_top_left.bmp"),
			"pipe2_hor_top_right":pyglet.image.load("./Lib/data/textures/pipe2_hor_top_right.bmp"),
			"pipe2_left_bot":pyglet.image.load("./Lib/data/textures/pipe2_left_bot.bmp"),
			"pipe2_left_top":pyglet.image.load("./Lib/data/textures/pipe2_left_top.bmp"),
			"pipe2_right_bot":pyglet.image.load("./Lib/data/textures/pipe2_right_bot.bmp"),
			"pipe2_right_top":pyglet.image.load("./Lib/data/textures/pipe2_right_top.bmp"),
			"pipe3_hor_bot_center":pyglet.image.load("./Lib/data/textures/pipe3_hor_bot_center.bmp"),
			"pipe3_hor_bot_left":pyglet.image.load("./Lib/data/textures/pipe3_hor_bot_left.bmp"),
			"pipe3_hor_bot_right":pyglet.image.load("./Lib/data/textures/pipe3_hor_bot_right.bmp"),
			"pipe3_hor_top_center":pyglet.image.load("./Lib/data/textures/pipe3_hor_top_center.bmp"),
			"pipe3_hor_top_left":pyglet.image.load("./Lib/data/textures/pipe3_hor_top_left.bmp"),
			"pipe3_hor_top_right":pyglet.image.load("./Lib/data/textures/pipe3_hor_top_right.bmp"),
			"pipe3_left_bot":pyglet.image.load("./Lib/data/textures/pipe3_left_bot.bmp"),
			"pipe3_left_top":pyglet.image.load("./Lib/data/textures/pipe3_left_top.bmp"),
			"pipe3_right_bot":pyglet.image.load("./Lib/data/textures/pipe3_right_bot.bmp"),
			"pipe3_right_top":pyglet.image.load("./Lib/data/textures/pipe3_right_top.bmp"),	
			"pipe4_left_bot":pyglet.image.load("./Lib/data/textures/pipe4_left_bot.bmp"),
			"pipe4_left_top":pyglet.image.load("./Lib/data/textures/pipe4_left_top.bmp"),
			"pipe4_right_bot":pyglet.image.load("./Lib/data/textures/pipe4_right_bot.bmp"),
			"pipe4_right_top":pyglet.image.load("./Lib/data/textures/pipe4_right_top.bmp"),	
			"pipe5_left_bot":pyglet.image.load("./Lib/data/textures/pipe5_left_bot.bmp"),
			"pipe5_left_top":pyglet.image.load("./Lib/data/textures/pipe5_left_top.bmp"),
			"pipe5_right_bot":pyglet.image.load("./Lib/data/textures/pipe5_right_bot.bmp"),
			"pipe5_right_top":pyglet.image.load("./Lib/data/textures/pipe5_right_top.bmp"),
			"pipe6_left_bot":pyglet.image.load("./Lib/data/textures/pipe6_left_bot.bmp"),
			"pipe6_left_top":pyglet.image.load("./Lib/data/textures/pipe6_left_top.bmp"),
			"pipe6_right_bot":pyglet.image.load("./Lib/data/textures/pipe6_right_bot.bmp"),
			"pipe6_right_top":pyglet.image.load("./Lib/data/textures/pipe6_right_top.bmp"),	
		}
		self.labelbatch = pyglet.graphics.Batch()
		self.labels = []

		self.sprites = []
		self.blocks = []
		self.load_world()


		update.register(self)

	def check_colision(self,x_pos,y_pos,width,height,axis=">"):
		if axis == ">":
			for x,y in self.blocks:
				if y_pos + height > y and y_pos < y + self.scale:
					if x_pos + width > x and x_pos < x + self.scale:
						return x,y

		if axis == "<":
			for x,y in self.blocks:
				if y_pos + height > y and y_pos < y + self.scale:
					if x_pos < x + self.scale and x_pos + width > x:
						return x,y

		if axis == "^":
			for x,y in self.blocks:
				if x_pos+width > x and x_pos < x + self.scale:
					if y_pos + height > y and y_pos < y + self.scale:
						return x,y
					
		if axis == "v":
			for x,y in self.blocks:
				if x_pos+width > x and x_pos < x + self.scale:
					if y_pos < y + self.scale and y_pos > y:
						return x,y+self.scale
		return None,None
	
	def overlap(self,x_pos,y_pos,width,height):
		for x,y in self.blocks:
			XA1 = x_pos
			XA2 = x_pos + width 
			XB1 = x	
			XB2 = x + self.scale
			YA1 = y_pos
			YA2 = y_pos + height
			YB1 = y
			YB2 = y + self.scale
			SI = max(0, min(XA2, XB2) - max(XA1, XB1)) * max(0, min(YA2, YB2) - max(YA1, YB1))
			S=(width*height)+(32*32)-SI
			if SI/S > 0:
				return SI/S
		return 0

	def load_world(self):
		self.world = worlds.worlds[self.world_number][self.world_subnumber]
		if self.world["background"] == "overworld":
			glClearColor(0.361,0.58,0.988,1)
		elif self.world["background"] == "underworld":
			glClearColor(0,0,0,1)
		elif self.world["background"] == "underwater":
			glClearColor(0.125,0.22,0.925,1)
		else:
			raise ValueError("invalid world type")

		for y,i in enumerate(reversed(self.world["background_blocks"])):
			for x,j in enumerate(i):
				if j == None:
					continue
				self.sprites.append(pyglet.sprite.Sprite(self.texturedb[j],x=x*self.scale,y=y*self.scale,batch=self.background_batch))

		largestx = 0
		largesty = 0
		for y,i in enumerate(reversed(self.world["foreground_blocks"])):
			for x,j in enumerate(i):
				if j == None:
					continue
				self.blocks.append((x*self.scale,y*self.scale))
				self.sprites.append(pyglet.sprite.Sprite(self.texturedb[j],x=x*self.scale,y=y*self.scale,batch=self.foreground_batch))
				if x > largestx:
					largestx = x
			if y > largesty:
				largesty = y
		self.width = largestx * self.scale
		self.height = largesty * self.scale

		for x,y in self.blocks:
			self.labels.append(pyglet.text.Label(text="{}\n{}".format(x,y),x=x,y=y+self.scale//2,bold=True,color=(0,0,0,255),width=self.scale,batch=self.labelbatch,multiline=True))

	def update(self,dt):
		pass

	def draw(self):
		glLoadIdentity()
		glTranslatef(self.scroll_x,self.scroll_y, 0)
		self.background_batch.draw()
		self.foreground_batch.draw()
		# self.labelbatch.draw()