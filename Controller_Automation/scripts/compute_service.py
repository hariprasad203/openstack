#Automation script for Installing compute service
import os
import sys
import commands
from configparser import RawConfigParser
import config1

config = RawConfigParser()

class COMPUTE_SERVICE(config1.IDENTITY):

    def ADD(self):
        print('configuring compute  service')
        count =0
        config_path = os.path.realpath('Config_files')
        config_path += '/config_system.ini'
        config.read(config_path)
        for section1 in config.sections():
            if section1 == 'Compute service':
                for option1 in config.options(section1):
                    value1 = config.get(section1 , option1)
		    Inifile_path = os.path.realpath('Config_files')
                    Inifile_path = Inifile_path + '/' + option1
		    if value1 == 'admin.ini':
			super(COMPUTE_SERVICE,self).run_admin_environment_variables()
                    elif value1.startswith('/etc'):
                        if value1 == "/etc/httpd/conf.d/00-nova-placement-api.conf":
                            super(COMPUTE_SERVICE,self).placement(Inifile_path, value1)
                        else:
                            super(COMPUTE_SERVICE,self).parsing_sections(Inifile_path,value1)
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




