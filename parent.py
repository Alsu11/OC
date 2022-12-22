import os
import sys
import random


def child():
    ch = os.fork()
    if ch == 0:
        argument = str(random.randint(5, 10))
        os.execl("./child.py", "child.py", argument)
    print(f"Parent [{os.getpid()}]: I ran children process with PID {ch}")


child_number = sys.argv[1]
child_number = int(child_number)

for i in range(0, child_number):
    child()

while child_number > 0:
    child_pid, status = os.wait()
    status = status / 256
    status = int(status)
    print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.")

    if status == 0:
        child_number = child_number - 1
    else:
        child()