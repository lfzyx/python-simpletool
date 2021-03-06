#!/usr/bin/env python3
#author lfzyx date 2015.11.16
import os
import datetime
import shutil
import sys
import time
import glob

if len(sys.argv) < 3:
    print("Usage:",sys.argv[0], "[DIR tomcat0 tomcat1...]")
    sys.exit(1)

rootpath = sys.argv[1]
if not rootpath.endswith("/"):
    rootpath += "/"

for project in sys.argv[2:]:
    sourcedir = rootpath + project + '/logs/'
    targetdir = rootpath + project + '/logs/' + (datetime.date(day=1, month= datetime.date.today().month, year= datetime.date.today().year) - datetime.timedelta(days=1)).strftime('%Y%m')

    try:
        os.makedirs(targetdir)
    except FileExistsError:
        print(sys.exc_info()[1])
    else:
        print ('Successfully created directory:', targetdir)

    for file in glob.glob(sourcedir + '*.[tlg]*'):
        #遍历源目录,找出后缀为log,txt,gz的文件,且文件的修改时间小于上个月最后一秒
        if  os.path.getmtime(file) < time.mktime(datetime.date(day=1, month= datetime.datetime.today().month, year= datetime.datetime.today().year).timetuple()):
            try:
                shutil.move(file, targetdir)
            except shutil.Error:
                print(sys.exc_info()[1])
            else:
                print("Successfully moved file:", file)
