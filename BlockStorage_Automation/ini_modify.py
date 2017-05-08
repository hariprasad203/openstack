import glob
import os
import sys
import fileinput
from configparser import RawConfigParser
def main():
	path = os.path.realpath('Config_files')
	path = path +"/*.ini"
	config = RawConfigParser()
	config.optionxform=str
	config.read(os.path.abspath('replace.ini'))
	list_files = glob.glob(path)
	for file_name in list_files:
		for section in config.sections():
			for key in config.options(section):
				value = config.get(section, key)
				fun(file_name, key, value)
			
def fun(file_name, key, value): 
	file1 = fileinput.FileInput(file_name, inplace=1)
	for line in file1:
		if key in line: 
			line = line.replace(key, value)
		sys.stdout.write(line)
	file1.close()

main()
