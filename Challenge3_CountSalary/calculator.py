#!/usr/bin/env python3

import sys

class Config(object):
	def __init__(self, configfile):
		self._config = {}
		with open(configfile) as file:
			for str in file:
				name,num = str.split('=')
				self._config[name.strip()] = num.strip()
		#for key, value in self._config.items():
			#print(key +' ' +value)
	
	def get_config(self,category):
		return self._config[category]

	def get_ensu_rate(self):
		ensu_rate = 0.00
		for key, value in self._config.items():
			value_f = float(value)
			if value_f < 1.00:
				ensu_rate += value_f
#		print("total ensu rate is ", ensu_rate)
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

#		for key, value in self.userdata.items():
#			print(key + ' ' + value)
	

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
			

if __name__ == '__main__':
	index = len(sys.argv)
	#print("len is ", index)
	if len(sys.argv) != 7:
		print("Parameter is not 7")
		quit()
	#print("OK---")
	if '-c' not in sys.argv:
		print("There is no -c")
		quit()
	if '-d' not in sys.argv:
		print("There is no -d")
		quit()
	if '-o' not in sys.argv:
		print("There is no -o")
		quit()
	args = sys.argv[1:]
	index_c = args.index('-c')
#	print("config file is ", args[index_c+1])
	tex_config = Config(args[index_c + 1])
	index_d = args.index('-d')
#	print("user file is ", args[index_d + 1])
	sal_data = UserData(args[index_d + 1])
	taxl = tex_config.get_config("JiShuL")
	taxh = tex_config.get_config("JiShuH")
	ensu_rate = tex_config.get_ensu_rate()	
	salary_data = sal_data.userdata
	index_o = args.index('-o')
	outfile = args[index_o +1]
	with open(outfile, 'w') as file:
		for no, sal in salary_data.items():
			ensurance = calcu_ensurance(taxl, taxh, ensu_rate, sal)
			total_tax = calcu_tax(sal, ensurance)
			income = float(sal) - ensurance - total_tax
			'''
			print("info of no :", no)
			print("salary is : " + '{:.2f}'.format(float(sal)))
			print("ensu is:" + '{:.2f}'.format(ensurance))
			print("total tax is " + '{:.2f}'.format(total_tax))
			print("income is " + '{:.2f}'.format(income))
			'''
			
			'''
			result = "%d%.2f%.2f%.2f%.2f"%(int(no),float(sal),ensurance,total_tax,income)			
			file.writelines(result)
			'''
			'''
			sal_list = []
			sal_list.append(int(no))
			sal_list.append(float("%.2f"%(float(sal))))
			sal_list.append(float("%.2f"%(ensurance)))
			sal_list.append(total_tax)
			sal_list.append(income)
			
			file.writelines(str(sal_list))
	
			'''
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
#		print("End of the py")

