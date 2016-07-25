# -*- coding:utf8 -*-

from __future__ import division
import math
import random


sessionVec = []
sessionItem = ""
dedupMap = {}
fileHandle = open("../data/train_cikm2014","r")
outfileHandle = open("../data/train_cikm2014_out","w")

while 1:
    fileline = fileHandle.readline()
    #print fileline
    if len(fileline) <= 0:
        break
    if len(fileline.strip()) == 0 :
        if len(sessionItem) != 0 :
            sessionVec.append(sessionItem)
            sessionItem = ""
            dedupMap = {}
        if len(sessionVec) == 10 :
            item = random.sample(sessionVec,1)
            outfileHandle.writelines(item)
            outfileHandle.writelines("\n")
            #print item
            #outfileHandle.("")
            sessionVec = []
        continue

    if fileline.find("CLASS=TEST") != -1 :
        continue
    lists = fileline.split("\t")
    classname = lists[0].split(" | ")
    if len(classname) == 2:
        if cmp(classname[0],classname[1]) > 0:
            fileline = classname[1]+" | "+ classname[0]+"\t"+lists[1]+"\t"+lists[2]+"\n"
    if fileline not in dedupMap:
        dedupMap[fileline] = ""
        sessionItem += fileline

classMap = {}
fileHandle = open("../data/train_cikm2014_out","r")
total = 0
while 1:
    fileline = fileHandle.readline()
    if len(fileline) == 0:
        break
    fileline = fileline.strip()
    if len(fileline) == 0:
        continue
    lines = fileline.split("\t")
    if len(lines) < 3 :
        continue
    if lines[0] not in classMap:
        classMap[lines[0]] = 1
    else:
        classMap[lines[0]] += 1
    total+=1
print classMap
print total