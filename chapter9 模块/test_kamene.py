#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

ping_result = sr1(IP(dst='8.8.8.8')/ICMP(), timeout=2, verbose=False)
ping_result.show()

