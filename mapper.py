#!/usr/bin/python
# -*-coding:utf-8 -*
from __future__ import print_function
import sys

for line in sys.stdin:
    print(line)


# for line in sys.stdin:
# 	# print(line)


# 	try:
# 		vid,uploader,age,category,other = line.split("\t",4)
# 	except:
# 		continue
# 	print(category,uploader,other, sep="\t")