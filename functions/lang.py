################################################
#CONSTANTS
################################################

DIGITS = "0123456789"

################################################
#ERRORS
################################################

class Error:
	def __init__(self, error_name, details):
		self.details = details
		self.error_name = error_name

	def as_string(self): 
		return f"{self.error_name}: {self.details}"

class InvalidCharacterError(Error):
	def __init__(self, details):
		super().__init__("Invalid Character", details)

################################################
#TOKENS
################################################

TT_INT = "integer"
TT_FLOAT = "float"
TT_PLUS = "plus"
TT_MINUS = "minus"
TT_MULTIPLY = "multiply"
TT_DIVIDE = "divide"
TT_L_PARENTHESIS = "left-paranthesis"
TT_R_PARENTHESIS = "right-paranthesis"

class Token:
	def __init__(self, type_, value=None):
		self.type = type_
		self.value = value
		
	def __repr__(self):
		if self.value: return f"{self.type}:{self.value}"
		else: return self.type
		
################################################
#LEXER
################################################

class Lexer:
	def __init__(self, text):
		self.text = text
		self.position = -1
		self.current_character = None
		self.advance()
		
	def advance(self):
		self.position += 1
		self.current_character = self.text[self.position] if self.position < len(self.text) else None

	def get_tokens(self):
		tokens = []
		while self.current_character != None:
			if self.current_character in " \t": self.advance()
			elif self.current_character in DIGITS: tokens.append(self.return_number_type())
			elif self.current_character == "+": tokens.append(Token(TT_PLUS)); self.advance()
			elif self.current_character == "-": tokens.append(Token(TT_MINUS)); self.advance()
			elif self.current_character == "*": tokens.append(Token(TT_MULTIPLY)); self.advance()
			elif self.current_character == "/": tokens.append(Token(TT_DIVIDE)); self.advance()
			elif self.current_character == "(": tokens.append(Token(TT_L_PARENTHESIS)); self.advance()
			elif self.current_character == ")": tokens.append(Token(TT_R_PARENTHESIS)); self.advance()
			else: self.advance(); return [], InvalidCharacterError('"' + self.current_character + '"')
		return tokens, None

	def return_number_type(self):
		decimal_count = 0
		number_in_string = ""
		while self.current_character != None and self.current_character in DIGITS + ".":
			if self.current_character == ".":
				if decimal_count == 1: break
				decimal_count += 1
				number_in_string += "."
			else: number_in_string += self.current_character
			self.advance()
		if not decimal_count: return Token(TT_INT, int(number_in_string))
		else: return Token(TT_FLOAT, float(number_in_string))

################################################
#RUN
################################################

def run(text):
	lexer = Lexer(text)
	tokens, error = lexer.get_tokens()
	return tokens, error