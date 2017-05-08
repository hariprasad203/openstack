#Automation script for Installing identity service
import os
import sys
import config1
import commands


from configparser import RawConfigParser
config = RawConfigParser()

class IDENTITY_SERVICE(config1.IDENTITY):
    
    def ADD(self):
        print('configuring identity service')
        count =0
        config_path = os.path.realpath('Config_files')
        config_path += '/config_system.ini'
        config.read(config_path)
        for section1 in config.sections():
            if section1 == 'Identity service':
                for option1 in config.options(section1):
                    value1 = config.get(section1 , option1)
                    Inifile_path1 = os.path.realpath('Config_files')
                    Inifile_path1  += '/' + option1
		    if value1 == 'admin.ini':
			 super(IDENTITY_SERVICE,self).run_admin_environment_variables()
                    elif value1.startswith('/etc'):
                        if value1 == '/etc/httpd/conf/httpd.conf':
                            super(IDENTITY_SERVICE,self).http(Inifile_path1,value1)
                        else:
                            super(IDENTITY_SERVICE,self).parsing_sections(Inifile_path1,value1)
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
