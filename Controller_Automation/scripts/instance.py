#Automation script for Configuring Launch Instance service
import os

import config1

from configparser import RawConfigParser
config = RawConfigParser()

class INSTANCE_SERVICE(config1.IDENTITY):
    
    def ADD(self):
        print('configuring Launch instace service')
        count =0
        config_path = os.path.realpath('Config_files')
        config_path += '/config_system.ini'
        config.read(config_path)
        for section in config.sections():
            if section == 'Launch an instance':
                for key in config.options(section):
		    value = config.get(section, key)
		    if value == 'admin.ini':
			super(INSTANCE_SERVICE,self).run_admin_environment_variables()
		    elif value == 'demo.ini':
			super(INSTANCE_SERVICE,self).run_demo_environment_variables()
                    else:
                        os.system(value)
                        count += 1
                        print "[OK] command "+str(count)+" runing successfully."
