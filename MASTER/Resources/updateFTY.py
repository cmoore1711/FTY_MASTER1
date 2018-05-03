import os


try:
    updateString = "sudo sh Desktop/FTY_MASTER1/MASTER/Resources/piUpdate.sh"
    os.system(updateString)
except:
    print('Error')
