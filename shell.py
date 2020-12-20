import os, sys
sys.path.insert(1, os.getcwd() + "/functions")
import lang

while True:
	text = input("#")
	result, error = lang.run(text)
	if error: print(error.as_string())
	else: print(result)