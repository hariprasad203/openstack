#Automation script for Configuring dashboard service
import os
from configparser import RawConfigParser
import config1
config = RawConfigParser()

class DASHBOARD_SERVICE(config1.DASHBOARD):
    
    def ADD(self):
        print('configuring dashboard service')
        count =0
        config_path = os.path.realpath('Config_files')
        config_path += '/config_system.ini'
        config.read(config_path)
        for section1 in config.sections():
            if section1 == 'Dashboard':
                for option1 in config.options(section1):
                    value1 = config.get(section1 , option1)
                    if value1.startswith('/etc'):
                        Inifile_path = os.path.realpath('Config_files')
                        Inifile_path = Inifile_path + '/' + option1
                        super(DASHBOARD_SERVICE,self).dashboard(Inifile_path,value1)
                    else:
                        os.system(value1)
                        count += 1
                        print "[OK] command "+str(count)+" runing successfully."
