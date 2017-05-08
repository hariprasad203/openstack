import os
import sys
import fileinput
import netifaces
from configparser import RawConfigParser

from scripts import config1
from scripts import host_networking
from scripts import network_time_protocol
from scripts import openstack_packages
from scripts import compute_service
from scripts import networking_service
from scripts import list_file
from scripts import ini_files

class main():
	def host_call(self):
		service = host_networking.HOST_NETWORKING()
		service.ADD()
		
	def ntp_call(self):
		service = network_time_protocol.NETWORK_TIME_PROTOCOL()
		service.ADD()

	def openstack_packages_call(self):
		service=openstack_packages.OPENSTACK_PACKAGES()
		service.ADD()

	def compute_call(self):
                service=compute_service.COMPUTE_SERVICE()
                service.ADD()

	def networking_call(self):
                service=networking_service.NETWORKING_SERVICE()
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

try:
	main_object=main()
	main_object.modify_ini_call()
	'''main_object.host_call()
	main_object.ntp_call()
	main_object.openstack_packages_call()
	main_object.compute_call()
	main_object.linux_bridege_ifconfig()
	main_object.networking_call()'''
	main_object.no_modify_ini_call()

except Exception as e:
	print str(e)
	print('Openstack installation error')
