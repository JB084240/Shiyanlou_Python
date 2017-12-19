#!/usr/bin/env python3

import sys

class Config(object):
	def __init__(self, configfile):
		self._config = {}
		with open(configfile) as file:
			for str in file:
				name,num = str.split('=')
				self._config[name.strip()] = num.strip()
	
	def get_config(self,category):
		return self._config[category]

	def get_ensu_rate(self):
		ensu_rate = 0.00
		for key, value in self._config.items():
			value_f = float(value)
			if value_f < 1.00:
				ensu_rate += value_f
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

def calcu_ensurance(taxl,taxh,ensu_rate,sal):
	tax_ens = 0.00
	sal_f = float(sal)
	if sal_f < float(taxl):
		tax_ens = float(taxl) * ensu_rate
	elif sal_f > float(taxh):
		tax_ens = float(taxh) * ensu_rate
	else:
		tax_ens = sal_f * ensu_rate
	return tax_ens

def calcu_tax(sal,ensurance):
	tax = 0.00
	sal_after = float(sal) - ensurance - 3500
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
	return tax
			

	index_d = args.index('-d')
	sal_data = UserData(args[index_d + 1])
	salary_data = sal_data.userdata
	index_o = args.index('-o')
	outfile = args[index_o +1]
	with open(outfile, 'w') as file:
		for no, sal in salary_data.items():
			ensurance = calcu_ensurance(taxl, taxh, ensu_rate, sal)
			total_tax = calcu_tax(sal, ensurance)
			income = float(sal) - ensurance - total_tax
	
			file.write(no)
			file.write(',')
			file.write("%.2f"%(float(sal)))
			file.write(',')
			file.write("%.2f"%(float(ensurance)))
			file.write(',')
			file.write("%.2f"%(float(total_tax)))
			file.write(',')
			file.write("%.2f"%(float(income)))

			file.write('\n')


def readData():	
	args = sys.argv[1:]
	index_c = args.index('-c')
	tex_config = Config(args[index_c + 1])

	taxl = tex_config.get_config("JiShuL")
	taxh = tex_config.get_config("JiShuH")
	ensu_rate = tex_config.get_ensu_rate()	

def getData():


def main():
	process1(target=readData).start()
	process2(target=f2).start()
	process3(target=f3).start()

if __name__ == '__main__':
	index = len(sys.argv)
	if len(sys.argv) != 7:
		print("Parameter is not 7")
		quit()
	if '-c' not in sys.argv:
		print("There is no -c")
		quit()
	if '-d' not in sys.argv:
		print("There is no -d")
		quit()
	if '-o' not in sys.argv:
		print("There is no -o")
		quit()
	main()
