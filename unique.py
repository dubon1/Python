#!/usr/bin/python3

from time import localtime
datetime_stamp='%4d-%02d-%02dT%02d-%02d-%02d' % localtime()[:6]
title='SysALogs'
ext='csv'
print('Unique filename: %s-%s.%s' % (title, datetime_stamp, ext))

