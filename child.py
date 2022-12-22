import sys
import os
import time
import random


sleep = sys.argv[1]
sleep = int(sleep)
process = os.getpid()
parent_process = os.getppid()
print(f"Child [{process}]: I am started. My PID {process}. Parent PID {parent_process}")
time.sleep(sleep)
print(f"Child [{process}]: I am ended. PID {process}. Parent PID {parent_process}")
exit_status = random.randint(0, 1)
sys.exit(exit_status)