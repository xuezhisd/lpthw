class Room(object):
	def __init__(self, name, description):
		self.name = name
		self.descritpion = descritpion
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)

		