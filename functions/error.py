class Error:
	def __init__(self, position_start, position_end, error_name, details):
		self.details = details
		self.error_name = error_name
		self.position_end = position_end
		self.position_start = position_start

	def as_string(self): 
		return f"File {self.position_start.filename}, line {self.position_start.line}:\n{self.error_name}: {self.details}"

class InvalidCharacterError(Error):
	def __init__(self, position_start, position_end, details):
		super().__init__(position_start, position_end, "Invalid Character", details)