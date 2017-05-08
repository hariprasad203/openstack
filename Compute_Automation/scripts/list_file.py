import glob
import os
import sys
import fileinput
import config1
from configparser import RawConfigParser

class MODIFY_INI_FILES(config1.IDENTITY):
	 def ADD(self):
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
					super(MODIFY_INI_FILES, self).ini_modify(file_name, key, value)
			
	


