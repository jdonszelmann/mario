import pyglet

window = ...
update = ...
keys = ...

def init(win,upd,kb):
	global window, update, keys
	window = win
	update = upd
	keys = kb


class Enemy:
	def __init__(self):
		assert window