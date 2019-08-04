import pysftp
import glob
import os
import time
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None   
with pysftp.Connection(host="dtn.sherlock.stanford.edu", username="orlovsky", password="Amway921@", cnopts=cnopts) as sftp:
    for i in range(10):
        for file in glob.glob("*.avi"):
            sftp.put(file)
            print(file)
            time.sleep(0.01)
            os.remove(file)
            i+=1

    
