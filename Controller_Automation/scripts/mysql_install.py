#Automation script for Installing Block storage service
import os
import sys
import commands
from configparser import RawConfigParser
import config1
config = RawConfigParser()

class MySql_Install(config1.IDENTITY):
    
    def ADD(self):
        print('MySql Installation')
        count =0
        config_path = os.path.realpath('Config_files')
        config_path += '/config_system.ini'
        config.read(config_path)
        for section1 in config.sections():
            if section1 == 'MySql':
                for option1 in config.options(section1):
                    value1 = config.get(section1 , option1)
                    if value1.startswith('/etc'):
                            Inifile_path = os.path.realpath('Config_files')
                            Inifile_path = Inifile_path + '/' + option1
                            super(MySql_Install,self).parsing_sections(Inifile_path,value1)
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
