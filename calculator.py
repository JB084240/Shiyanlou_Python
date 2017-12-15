#!/usr/bin/env python3

import sys

class Config(object):
	def __init__(self, configfile):
		with open(configfile) as file:
			self.rate = 0.00
			for str in file:
				print(str)
				str.strip()
				name,num = str.split('=')
				print(name,end='')
				print(num)	
				if name == "JiShuL":
					self.lowest = float(num)
				elif name == "JiShuH":
					self.highest = float(num)
				else:
					self.rate += float(num)
				

if __name__ == '__main__':
	args = sys.argv[1:]
	index_c = args.index('-c')
	print("file is ",args[index_c+1])
	tex_config = Config(args[index_c+1])
