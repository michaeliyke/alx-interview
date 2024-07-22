#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(
            1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

# 180.136.89.37 - [2024-07-22 03:28:33.372750] "GET /projects/260 HTTP/1.1" 401 112
# 255.118.168.51 - [2024-07-22 03:28:34.203744] "GET /projects/260 HTTP/1.1" 403 71
# 106.218.172.177 - [2024-07-22 03:28:34.771727] "GET /projects/260 HTTP/1.1" 200 874
