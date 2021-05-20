#!/usr/bin/python3.7
import signal
import sys
import os
import platform
import time
import subprocess

def dif(a, b):
    txt1 = a
    txt2 = b
    with open(txt1) as infile:
        f1 = infile.readlines()
    with open(txt2) as infile:
        f2 = infile.readlines()
    only_in_f1 = [i for i in f1 if i not in f2]
    only_in_f2 = [i for i in f2 if i not in f1]
    with open('different.txt', 'w') as outfile:
        if only_in_f1:
            outfile.write('Process stop working:\n')
            for line in only_in_f1:
                outfile.write(line)

        if only_in_f2:
            outfile.write('Process start working:\n')
            for line in only_in_f2:
                outfile.write(line)



def findpos(date1, date2):
    lines = []
    flag = True
    fout = open("one", "w+")
    for line in open("serviceList").readlines():
        if 'The date and time is: ' in line:
            if flag:
                if date1 in line:
                    flag = False
            else:
                break
        elif not flag:
            fout.write(line)
    
    fout = open("two", "w+")
    lines = []
    flag = True
    for line in open("serviceList").readlines():
        if 'The date and time is: ' in line:
            if flag:
                if date2 in line:
                    flag = False
            else:
                break
        elif not flag:
            fout.write(line)
    


