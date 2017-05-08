#Automation script for Installing Block storage service
import os
import sys
import commands
from configparser import RawConfigParser
import config1
config = RawConfigParser()

class BLOCK_STORAGE_SERVICE(config1.IDENTITY):
    
    def ADD(self):
        print('configuring block storage service')
        count =0
        config_path = os.path.realpath('Config_files')
        config_path += '/config_system.ini'
        config.read(config_path)
        for section1 in config.sections():
            if section1 == 'Block storage':
                for option1 in config.options(section1):
                    value1 = config.get(section1 , option1)
		    if value1 == 'admin.ini':
			super(BLOCK_STORAGE_SERVICE,self).run_admin_environment_variables()
                    elif value1.startswith('/etc'):
                            Inifile_path = os.path.realpath('Config_files')
                            Inifile_path = Inifile_path + '/' + option1
                            super(BLOCK_STORAGE_SERVICE,self).parsing_sections(Inifile_path,value1)
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
