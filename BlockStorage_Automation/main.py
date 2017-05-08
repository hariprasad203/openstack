import os
import sys
import fileinput
from configparser import RawConfigParser

from scripts import config1
from scripts import host_networking
from scripts import network_time_protocol
from scripts import openstack_packages
from scripts import block_storage
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

	def block_storage_call(self):
                service=block_storage.BLOCK_STORAGE_SERVICE()
                service.ADD()
	def modify_ini_call(self):
		service=list_file.MODIFY_INI_FILES()
		service.ADD()
	def no_modify_ini_call(self):
		service=ini_files.NO_MODIFY_INI_FILES()
		service.ADD()


try:
	main_object=main()
	main_object.modify_ini_call()
	'''main_object.host_call()
	main_object.ntp_call()
	main_object.openstack_packages_call()
	main_object.block_storage_call()'''
	main_object.no_modify_ini_call()

except Exception as e:
	print str(e)
	print('Openstack installation error')
