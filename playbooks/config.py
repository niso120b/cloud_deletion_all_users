#!/usr/bin/python

import sys


if __name__ == '__main__':
	print '<<<<<<<<<< start of configuration for specific user >>>>>>>>>>'
	print 'Please enter the admin pass for openstack'
	admin_pass = raw_input()
	f = open('config_vars.yml', 'w')
	f.write('admin_pass: '+ admin_pass)
	print 'Enter the IP of the config node'
	config_IP = raw_input()
	print 'Enter the username for config node. e.g:root'
	config_user = raw_input()
	print 'Enter the password for above user in config node.'
	config_pass = raw_input()
	f = open('inventory', 'w')
	f.write('[cloud]\n')
	f.write('cloud1')
	f.write(' ')
	f.write('ansible_ssh_host=' + config_IP)
	f.write(' ')
	f.write('ansible_ssh_port=22')
	f.write(' ')
	f.write('ansible_ssh_user=' + config_user)
	f.write(' ')
	f.write('ansible_ssh_pass=' + config_pass)
	f.write(' ')
	f.write('ansible_sudo_pass=' + config_pass)
	f.close()
	print '<<<<<<<<<< configuration is done >>>>>>>>>>'
	print '<<<<<<<<<< Now you can run this command: >>>>>>>>>> '
	print '<<<<<<<<<< ansible-playbook all_user_deletion.yml >>>>>>>>>>'
