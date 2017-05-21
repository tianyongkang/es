#!/usr/bin/python

import os
import datetime
import re
import sys


def sfcount_monitor(vname,nvalue):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    f = 'sfcount-monitor.%s.0.log' % today
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    r = open(f,'r').readlines()
    value_name = []
    value = []
    for i in r:
        v = i.strip().split(' ')
        date_now = v[0]+' ' + v[1]
        if date in date_now: 
            for i in range(2,len(v)):
                if i % 2 == 0:
                    value.append([v[i],v[i+1]])
                    if v[i] not in value_name:
                        value_name += [{'{#SFCOUNTNAME}':v[i]}]
                
    count = 0
    for i in value:
        if i[0] in value_name:
            if vname == i[0] and nvalue == "fail":
                count += int(i[1].split(',')[1])
    
    print count
    print value_name
sfcount_monitor('batchUpdate_quartz','fail')
#print value

    #print v
    #if date in v:
    #k = re.match('(?P<date>\d+-\d+-\d+ \d+:\d+:\d+,\d+) ((?P<para>\w+) (?P<success>\d+),(?P<fail>\d+) (?P<para02>\w+) (?P<success02>\d+),(?P<fail02>\d+)|(?P<para01>\w+) (?P<success01>\d+),(?P<fail01>\d+))',v)
    #key.append(k.group("para"))
    #key.append(k.group("para01"))
    #key.append(k.group("para02"))
    #value_success.append(k.group("success"))
    #value_success.append(k.group("success01"))
    #value_success.append(k.group("success02"))
    #value_fail.append(k.group("fail"))
    #value_fail.append(k.group("fail01"))
    #value_fail.append(k.group("fail02"))


#print key
#key_para = []
#for i in key:
#    if i is not None:
#	   key_para.append(i)



#value01 = []
#for i in value_success:
#    if i is not None:
#	value01.append(i)

#value02 = []
#for i in value_fail:
#    if i is not None:
#	value02.append(i)




#last = zip(key_para,value01,value02)

#success_updateSchoolSynchro = []
#fail_updateSchoolSynchro = []
#success_findSchoolSynchro_02 = []
#fail_findSchoolSynchro_02 = []
#success_batchUpdate_quartz = []
#fail_batchUpdate_quartz = []

#for k,c,f in last:
#    if k == "updateSchoolSynchro":
#	success_updateSchoolSynchro.append(int(c))
#	fail_updateSchoolSynchro.append(int(f))
#    elif k == "findSchoolSynchro_02":
#	success_findSchoolSynchro_02.append(int(c))
#	fail_findSchoolSynchro_02.append(int(f))
#    elif k == "batchUpdate_quartz":
#	success_batchUpdate_quartz.append(int(c))
#	fail_batchUpdate_quartz.append(int(f))

#if sys.argv[1] == "updateSchoolSynchro" and sys.argv[2] == "success":
#    print sum(success_updateSchoolSynchro)
#elif sys.argv[1] == "findSchoolSynchro_02" and sys.argv[2] == "success":
#    print sum(success_findSchoolSynchro_02)
#elif sys.argv[1] == "batchUpdate_quartz" and sys.argv[2] == "success":
#    print sum(success_batchUpdate_quartz)
#elif sys.argv[1] == "updateSchoolSynchro" and sys.argv[2] == "fail":
#    print sum(fail_updateSchoolSynchro)
#elif sys.argv[1] == "findSchoolSynchro_02" and sys.argv[2] == "fail":
#    print sum(fail_findSchoolSynchro_02)
#elif sys.argv[1] == "batchUpdate_quartz" and sys.argv[2] == "fail":
#    print sum(fail_batchUpdate_quartz)

