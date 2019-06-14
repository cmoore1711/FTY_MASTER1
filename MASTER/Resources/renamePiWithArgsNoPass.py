import sys
import subprocess
import time
import os

#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)

#new_name = str(sys.argv[1])
cmd = "hostname"
currDeviceName = subprocess.check_output(cmd, shell = True ).decode('ascii').rstrip('\n').split(' ')[0]


new_name = input("What should the new name be? ")
if(new_name != ''):
    with open('/etc/hosts', 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(currDeviceName, new_name)

    # Write the file out again
    with open('/etc/hosts', 'w') as file:
      file.write(filedata)


    with open('/etc/hostname', 'r') as file     :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(currDeviceName, new_name)

    # Write the file out again
    with open('/etc/hostname', 'w') as file:
      file.write(filedata)
    print('Done! Will reboot in 5 seconds.')
    time.sleep(5)
    os.system('reboot')

else:
    print('Cancelled')
