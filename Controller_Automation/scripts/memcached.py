#Automation script for Memcached
import os
import sys
import config1
import commands


from configparser import RawConfigParser
config = RawConfigParser()

class MEMCACHED(config1.MEMCAHED):

    def ADD(self):
        print('configuring memcached')
        count =0
        config_path = os.path.realpath('Config_files')
        config_path += '/config_system.ini'
        config.read(config_path)
        for section1 in config.sections():
            if section1 == 'Memcached':
                for option1 in config.options(section1):
                    value1 = config.get(section1 , option1)
                    if value1.startswith('/etc'):
                        Inifile_path = os.path.realpath('Config_files')
                        Inifile_path = Inifile_path + '/' + option1
                        super(MEMCACHED,self).memcache(Inifile_path,value1)
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
