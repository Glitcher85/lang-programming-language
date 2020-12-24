class Position:
	def __init__(
		self, index, 
		line, column, 
		filename, filetext
	):
		self.line = line
		self.index = index
		self.column = column
		self.filename = filename
		self.filetext = filetext

	def advance(self, current_character):
		self.index += 1
		self.column += 1
		if current_character == "\n": self.line += 1; self.column = 0
		return self

	def copy(self): 
		return Position(
			self.index, 
			self.line, 
			self.column, 
			self.filename, 
			self.filetext	
		)