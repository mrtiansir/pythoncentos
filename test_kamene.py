#!/usr/local/bin/python3
# _*_ coding=utf-8 _*_
# python basic scripts

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *

ping_pkt = IP(dst='8.8.8.8')/ICMP()
ping_result = sr1(ping_pkt, timeout=2, verbose=False)

ping_result.show()

