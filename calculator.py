#!/usr/bin/env python3

import sys

class Config(object):
	def __init__(self, configfile):
		self._config = {}
		with open(configfile) as file:
			for str in file:
				name,num = str.split('=')
				print(name)
				name.strip()
				num.strip()
				self._config[name] = num
		for key, value in self._config.items():
			print(key +' ' +value)
	
	def get_config(self):
		for key, value in self._config.items():
			if key == 'JiShuL':
				return value

	def get_ensu_rate(self):
		ensu_rate = 0.00
		for key, value in self._config.items():
		#	print("rate is ", value)
			value_f = float(value)
			if value_f < 1.00:
				ensu_rate += value_f
		print("total ensu rate is ", ensu_rate)
		return ensu_rate
				
class UserData(object):
	def __init__(self, userdatafile):
		self.userdata = {}
		self.no = 0
		with open(userdatafile) as file:
			for str in file:
				self.no += 1
				id,salary = str.split(',')
				self.userdata[id] = salary

		for key, value in self.userdata.items():
			print(key + ' ' + value)
	

def calcu_ensurance(taxl,taxh,ensu_rate,sal):
	tax_ens = 0.00

	if sal < taxl:
		tax_ens = taxl * ensu_rate
	elif sal > taxh:
		tax_ens = taxh * ensu_rate
	else:
		tax_ens = sal * ensu_rate
	print("total ensurace is ", tax_ens)
	return tax_ens

def calcu_tax(sal,ensurance):
	tax = 0.00
	sal_after = sal - ensurnce - 3500
	if sal_after <= 0:
		tax = 0.00
	elif sal_after <= 1500:
		tax = sal_after * 0.03
	elif sal_after > 1500 and sal_after <= 4500:
		tax = sal_after * 0.10 - 105
	elif sal_after > 4500 and sal_after <= 9000:
		tax = sal_after * 0.20 - 555
	elif sal_after > 9000 and sal_after <= 35000:
		tax = sal_after * 0.25 - 1005
	elif sal_after > 35000 and sal_after <= 55000:
		tax = sal_after * 0.30 - 2755
	elif sal_after > 55000 and sal_after <= 80000:
		tax = sal_after * 0.35 - 5505
	else:
		tax = sal_after * 0.45 - 13505
	print("total tax is ", tax)
	return tax
			

if __name__ == '__main__':
	args = sys.argv[1:]
	index_c = args.index('-c')
	print("config file is ", args[index_c+1])
	tex_config = Config(args[index_c + 1])
	index_d = args.index('-d')
	print("user file is ", args[index_d + 1])
	sal_data = UserData(args[index_d + 1])
	taxl = tex_config.get_config("JiShuL")
	taxh = tex_config.get_config("JiShuH")
	ensu_rate = tex_config.get_ensu_rate()	
	salary_data = sal_data.userdata
	for no, sal in salary_data.items():
		ensurance = calcu_ensurance(taxl, taxh, ensu_rate, sal)
		print(no + "ensu is " + ensurance)
		total_tax = calcu_tax(sal, ensurance)
		print(no + "total tax is " + total_tax)

	print("End of the py")
