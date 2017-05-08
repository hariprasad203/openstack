#Automation script for Host Networking
import os
import sys
import fileinput
import config1

from configparser import RawConfigParser

class HOST_NETWORKING(config1.HOSTNAME):

        def ADD(self):
                print('setting hostname')
                count =0
		config = RawConfigParser()

		config_path = os.path.realpath('Config_files')
                config_path += '/config_system.ini'
		print(config_path)
		config.read(config_path)
		for section1 in config.sections():
                        if section1 == 'Host networking':
                                for option1 in config.options(section1):
                                        value1 = config.get(section1 , option1)
                                        if value1.startswith('/etc'):
						Inifile_path = os.path.realpath('Config_files')
						Inifile_path = Inifile_path + '/' + option1
						print(Inifile_path)
                                       		super(HOST_NETWORKING,self).hostname(Inifile_path,value1)
                                        else:
						os.system(value1)
                                                count += 1
                                                print "[OK] command "+str(count)+" runing successfully."




