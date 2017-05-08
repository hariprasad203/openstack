import os
import sys
import subprocess
import fileinput
from configparser import RawConfigParser
config = RawConfigParser()

class HOSTNAME(object):
    
    def hostname(self, key, value):
        path="chmod 777 "+value
        os.system(path)
        cnt=0
        with open(value , 'r') as file1:
            with open('/etc/temphosts', 'w+') as file2:
                for line1 in file1:
                    if cnt < 2:
                        file2.write(line1)
                        cnt = cnt+1
                    else:
                        break
        with open(key ,'r') as file3:
            with open('/etc/temphosts', 'a+') as file4:
                for line2 in file3:
                    file4.write(line2)
        os.system("cp /etc/temphosts /etc/hosts")
                
                
class NTP(object):
    def chrony_sources(self, key, value):
        path="chmod 777 "+value
        os.system(path)
        config = RawConfigParser()
        config.read(key)
        last_line_num= int(subprocess.check_output('wc -l %s' % value, shell=True).strip().split()[0])
        file = fileinput.FileInput(value, inplace=1)
        for section in config.sections():
            for option in config.options(section):
                server = config.get(section, option)
                server_found =0
                line_num = 0
                
                for line in file:
                    line_num = line_num + 1
                    if server in line and server_found == 0:
                        server_found =1
                    elif last_line_num == line_num and server_found == 0:
                        line = line.replace(line, line+server+'\n')
                    sys.stdout.write(line)
        file.close()


class MEMCAHED(object):
   def memcache(self,key,value):
        path="chmod 777 "+value
        os.system(path)
        config = RawConfigParser()
	config.optionxform=str
        config.read(key)
        for section in config.sections():
            for option in config.options(section):
                ip = config.get(section, option)
                for line in fileinput.FileInput(value, inplace=1):
                    line = line.replace("127.0.0.1", ip)
                    sys.stdout.write(line)

class IDENTITY(object):


    def ini_modify(self,file_name, key, value): 
	file1 = fileinput.FileInput(file_name, inplace=1)
	for line in file1:
	    if key in line: 
		line = line.replace(key, value)
	    sys.stdout.write(line)
    	file1.close()

    def run_admin_environment_variables(self):
	config = RawConfigParser()
	config.optionxform = str 
	path = os.path.realpath('Config_files')
	path += '/admin.ini'
	config.read(path)
	for section in config.sections():
	    for option in config.options(section):
		value=config.get(section, option)
		os.environ[option]=value


    def run_demo_environment_variables(self):
	config = RawConfigParser()
	config.optionxform = str 
	path = os.path.realpath('Config_files')
	path += '/demo.ini'
	config.read(path)
	for section in config.sections():
	    for option in config.options(section):
		value=config.get(section, option)
		os.environ[option]=value
    
    def add_section(self, filename, section):
        path="chmod 777 "+filename
        os.system(path)
        with open(filename, 'a+') as file:
            if section == 'MyDefault':
                default_found=0
                for line in file:
                    if '[DEFAULT]' in line and line.startswith('['):
                        default_found=1
                        break
                if default_found == 0:
                    section = 'DEFAULT'
                    file.write('['+section+']\n') 
            else:
                file.write('['+section+']\n') 
        file.close()
        
    def check_n_add_key(self, filename, section, key, value):
        
        if section == 'MyDefault':
            section = 'DEFAULT'
        section = '['+section+']'
        path="chmod 777 "+filename
        os.system(path)
        last_line_num= int(subprocess.check_output('wc -l %s' % filename, shell=True).strip().split()[0])
        file = fileinput.FileInput(filename, inplace=1)
        linefound=0
        written=0
        line_num=0
        for line in file:
            line_num = line_num + 1 
            if written==0 and linefound == 0 and line.startswith('[') and section in line :
                if line_num == last_line_num:
                    line=line.replace(line,line+"\n"+key+" = "+value+"\n")
                    written=1
                linefound=1
            elif written==0 and linefound ==1 and key in line and line.startswith(key):
                line = line.replace(line,key+" = "+value+"\n")
                written=1
            elif written==0 and linefound == 1 and line.startswith('['):
                line=line.replace("[",key+" = "+value+"\n\n[")
                written = 1
            elif written == 0 and linefound == 1 and last_line_num == line_num :
                line = line.replace(line, line + "\n" + key + " = " + value + "\n")
                written = 1
            sys.stdout.write(line)
        file.close()



    def placement(self, ini_file, config_file):
	path="chmod 777 "+ini_file
	path="chmod 777 "+config_file

	last_line_num= int(subprocess.check_output('wc -l %s' % config_file, shell=True).strip().split()[0])
    	found = 0
    	count = 0
    	with open(config_file , 'r') as file1:
            for l1 in file1:
        	if "#placement" in l1:
        	    found =1
        	    break
	    if found == 0 :
		path1 = "cp "+config_file+" /etc/tmp_place"
		os.system(path1)
		with open(ini_file ,'r') as file3:
                    with open('/etc/tmp_place', 'a+') as file4:
                	for line2 in file3:
                	    file4.write(line2)
	path = "cp /etc/tmp_place "+config_file
	os.system(path)


    def parsing_sections(self, ini_file, conf_file):
        config1 = RawConfigParser()
        config2 = RawConfigParser()
        config1.optionxform=str
        config2.optionxform=str
        config1.read(ini_file)
	files = config2.read(conf_file)
	if conf_file not in files:
		path = "touch "+conf_file
		os.system(path)
		config2.read(conf_file)

        for section in config1.sections():
            if not config2.has_section(section):
                self.add_section(conf_file, section)
        for section in config1.sections():
            for key in config1.options(section):
                value = config1.get(section, key)
                self.check_n_add_key( conf_file, section, key, value)
                
    def http(self, key, value):
        path="chmod 777 "+value
        os.system(path)
        with open(key, 'r') as file1:
            with open(value, 'a+') as file2:
                count = 0
                for line1 in file1:
                    for line2 in file2:
                        if line1 == line2:
                            count = 1
                            break
                    if count == 0:
                        file2.write(line1)
                        break


class DASHBOARD(object):
    
    def write_key(self, filename, key, value):
        path="chmod 777 "+filename
        os.system(path)
        last_line_num= int(subprocess.check_output('wc -l %s' % filename, shell=True).strip().split()[0])
        written=0
        line_num=0
        value_end=0
        file = fileinput.FileInput(filename, inplace=1)
        for line in file:
            line_num = line_num+1
            if written==0 and key in line and line.startswith(key):
                line = line.replace(line,key+" = "+value+"\n")
                written=1
            elif written==1 and value_end == 0:
                if line.startswith('#') or '=' in line or '\n' == line :
                    value_end = 1
                else:
                    line = line.replace(line, "")
            elif written==0 and last_line_num == line_num :
                line=line.replace(line, line +"\n"+key+" = "+value+"\n")
                written = 1
            sys.stdout.write(line)
        file.close()
    
    def dashboard(self , ini_file , conf_file):
        
        config=RawConfigParser()
        config.optionxform=str
        config.read(ini_file)
        for section in config.sections():
            for key in config.options(section):
                value = config.get(section, key)
                self.write_key(conf_file, key, value)


