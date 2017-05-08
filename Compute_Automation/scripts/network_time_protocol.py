#Automation script for Network time protocol
import os
import sys
import fileinput
import config1
import commands

from configparser import RawConfigParser

class NETWORK_TIME_PROTOCOL(config1.NTP):

	def ADD(self):
                print('network time protocol configuration')
                count =0
		config = RawConfigParser()
               
		config_path = os.path.realpath('Config_files')
                config_path += '/config_system.ini'
		config.read(config_path)
                for section1 in config.sections():
                        if section1 == 'Network Time Protocol':
                                for option1 in config.options(section1):
                                        value1 = config.get(section1 , option1)
                                        if value1.startswith('/etc'):
						Inifile_path = os.path.realpath('Config_files')
                                                Inifile_path = Inifile_path + '/' + option1
                                                print(Inifile_path)
                                                super(NETWORK_TIME_PROTOCOL,self).chrony_sources(Inifile_path,value1)
                                        else:
                                                os.system(value1)
						if 'status' in value1:
                                                        output = commands.getoutput(value1)
                                                        if 'running' in output:
                                                                print("service is up and running!")
                                                        else:
                                                                print('service is dead and inactive')
								sys.exit('service is dead and inactive')

                                                count += 1
                                                print "[OK] command "+str(count)+" runing successfully."




