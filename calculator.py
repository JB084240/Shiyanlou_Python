#!/usr/bin/env python3

import sys

class Config(object):
	def __init__(self, configfile):
		self._config = {}
		with open(configfile) as file:
			for str in file.readline:
				str.strip()
				name,num = str.split('=')
				print(name,num)	
				#if name == "JiShuL":
				#	self.lowest = int(num)
				#elif name == "JiShuH":
				#	self.highest = int(num)
				#else:
				#	self.rate += int(num)


if __name__ == '__main__':
	try:
		args = sys.argv[1:]
		index_c = args.index('-c')
		print("para %s is %s",index_c+1,args[index_c+1])
		tex_config = Config(args[index_c+1])
	except:
		print("parameter error")
