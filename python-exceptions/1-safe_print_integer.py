#!/usr/bin/python3
def safe_print_interger(value):
	try:
		print("{:d}".format(value))
		return Treu
	except (ValueError, TypeError):
		return False
