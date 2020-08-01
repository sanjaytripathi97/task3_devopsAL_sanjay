#!/usr/bin/python3

import os

cmd = os.popen("kubectl get pods | grep webserver")
cmd_op = cmd.read()
x = cmd_op.split('\n')
del x[-1]
for y in x:
    z = y.split()
    print(z)
    os.system("kubectl cp index.php {}:/var/www/html/".format(z[0]))
