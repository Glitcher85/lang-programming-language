from error import *
from token import Token
from position import Position

DIGITS = "0123456789"
TT_INTEGER = "integer"
TT_FLOAT = "float"
TT_PLUS = "plus"
TT_MINUS = "minus"
TT_MULTIPLY = "multiply"
TT_DIVIDE = "divide"
TT_L_PARENTHESIS = "left-paranthesis"
TT_R_PARENTHESIS = "right-paranthesis"

class Lexer:
	def __init__(self, filename, text):
		self.text = text
		self.filename = filename
		self.current_character = None
		self.position = Position(-1, 1, -1, filename, text)
		self.advance()
		
	def advance(self):
		self.position.advance(self.current_character)
		self.current_character = self.text[self.position.index] if self.position.index < len(self.text) else None

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
			else: 
				self.position_start = self.position.copy()
				return [], InvalidCharacterError(self.position_start, self.position, '"' + self.current_character + '"')
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
		if not decimal_count: return Token(TT_INTEGER, int(number_in_string))
		else: return Token(TT_FLOAT, float(number_in_string))