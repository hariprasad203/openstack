import os
import sys
import fileinput
import netifaces
from configparser import RawConfigParser

from scripts import host_networking
from scripts import network_time_protocol
from scripts import openstack_packages
from scripts import message_queue
from scripts import memcached
from scripts import identity_service
from scripts import image_service
from scripts import compute_service
from scripts import networking_service
from scripts import block_storage
from scripts import dashboard
from scripts import instance
from scripts import list_file
from scripts import mysql_install
from scripts import ini_files

class main():
	def host_call(self):
		service = host_networking.HOST_NETWORKING()
		service.ADD()
	def mysql_call(self):
		rc = subprocess.call("./sample.sh", shell=True)
		print(rc)
		
	def mysql_install(self):
		service=mysql_install.MySql_Install()
		service.ADD()

	def ntp_call(self):
		service = network_time_protocol.NETWORK_TIME_PROTOCOL()
		service.ADD()

	def openstack_packages_call(self):
		service=openstack_packages.OPENSTACK_PACKAGES()
		service.ADD()
		
	def message_call(self):
		service=message_queue.MESSAGE_QUEUE()
		service.ADD()
		
	def memcached_call(self):
		service=memcached.MEMCACHED()
		service.ADD()
		
	def identity_call(self):
		service=identity_service.IDENTITY_SERVICE()
		service.ADD()
		
	def image_call(self):
		service=image_service.IMAGE_SERVICE()
		service.ADD()
	
	def compute_call(self):
		service=compute_service.COMPUTE_SERVICE()
		service.ADD()

	def networking_call(self):
		service=networking_service.NETWORKING_SERVICE()
		service.ADD()
		
	def block_storage_call(self):
		service=block_storage.BLOCK_STORAGE_SERVICE()
		service.ADD()

	def dashboard_call(self):
		service=dashboard.DASHBOARD_SERVICE()
		service.ADD()
	def launch_instance_call(self):
		service=instance.INSTANCE_SERVICE()
		service.ADD()

	def modify_ini_call(self):
		service=list_file.MODIFY_INI_FILES()
		service.ADD()
	def no_modify_ini_call(self):
		service=ini_files.NO_MODIFY_INI_FILES()
		service.ADD()
	def linux_bridege_ifconfig(self):
		interface_list = netifaces.interfaces()
		path = os.path.realpath('Config_files')
		path += '/bridge.ini'
		file = fileinput.FileInput(path, inplace=1)
		for line in file:
			if 'PROVIDER_INTERFACE_NAME' in line:
				line=line.replace('PROVIDER_INTERFACE_NAME', interface_list[1])
			sys.stdout.write(line)
		file.close()

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
		
	
	def test(self):
		print( os.environ.get('OS_USERNAME') )


try:
	main_object=main()
	main_object.modify_ini_call()
	#main_object.mysql_install()
	#main_object.mysql_call()
	main_object.host_call()
	main_object.ntp_call()
	main_object.openstack_packages_call()
	main_object.message_call()
	main_object.memcached_call()
	main_object.run_admin_environment_variables()
	main_object.identity_call()
	main_object.run_admin_environment_variables()
	main_object.image_call()
	main_object.run_admin_environment_variables()
	main_object.compute_call()
	main_object.linux_bridege_ifconfig()
	main_object.run_admin_environment_variables()
	main_object.networking_call()
	main_object.run_admin_environment_variables()
	main_object.dashboard_call()
	main_object.run_admin_environment_variables()	
	main_object.block_storage_call()
	#main_object.launch_instance_call()
	#main_object.no_modify_ini_call()
	


except Exception as e:
	print str(e)
	print('Openstack installation error')
