#Automation script for installing and configuring openstack

import os
import sys
import fileinput

from configparser import RawConfigParser
config = RawConfigParser()

class OPENSTACK_PACKAGES():

	def ADD(self):
                print('configuring openstack packages')
                count =0
		config_path = os.path.realpath('Config_files')
                config_path += '/config_system.ini'
		config.read(config_path)
                for section1 in config.sections():
                        if section1 == 'Openstack packages':
                                for option1 in config.options(section1):
                                        value1 = config.get(section1 , option1)
                                        if value1.startswith('/etc'):
                                                pass
                                        else:
                                                os.system(value1)
                                                count += 1
                                                print "[OK] command "+str(count)+" runing successfully."




