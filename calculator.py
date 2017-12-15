#!/usr/bin/env python3

import sys

class Config(object):
	def __init__(self, configfile):
		with open(configfile) as file:
			self.rate = 0.00
			self.lowest = 0.00
			self.highest = 0.00
			for str in file:
				print(str)
				str.strip()
				name,num = str.split('=')
				print(type(name))
				print(name)
				if name == "JiShuL":
					self.lowest = float(num)
				elif name == "JiShuH":
					self.highest = float(num)
				else:
					self.rate += float(num)
			print("lowest is ", self.lowest)
			print("highest is ",self.highest)
			print("total rate is ", self.rate)
				

class UserData(object):
	def __init_(self, userdatafile):
		self.userdate = {}
		self.no = 0
		with open(userdatafile) as file:
			for str in file:
				self.no += 1
				print(str)
				id,salary = str.split(',')
				print(id,end='')
				print(salary)
				self.userdata[id] = float[salary]
	

#def calculator(nol,noh,rate,sal):
#	taxe = 0
#	if sal <
	
		
			

if __name__ == '__main__':
	args = sys.argv[1:]
	index_c = args.index('-c')
	print("config file is ", args[index_c+1])
	tex_config = Config(args[index_c + 1])
	print("user file is ", args[index_c + 3])
	sal_data = UserData(args[index_c + 3])
