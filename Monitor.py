#!/usr/bin/python3.7
import signal
import sys
import os
import platform
import time
import subprocess
import fox
def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    if os.path.exists("linux.txt"):
        os.remove("linux.txt")
    if os.path.exists("tee.txt"):
        os.remove("tee.txt")   

    sys.exit(0)
    



System=platform.system()
print("please choose mode: Manual or Monitor.")
mode = input()
while (mode!="Manual" and mode!="Monitor"):
    print("invalid input try again please.")
    mode=input()

if (mode == "Manual"):
    date1 = input('Please enter the first date(The recent date) to compare(at: %d/%m/%Y %H:%M:%S format): ')
    date2 = input('Please enter the second date(The old date) to compare(at: %d/%m/%Y %H:%M:%S format): ')
    fox.findpos(date1, date2)
    
    fox.dif("two", "one")
    os.system("rm one")
    os.system("rm two")
    os.system("cat different.txt")
    os.system("rm different.txt")

elif (mode == "Monitor"):
    print("please enter frequency in seconds to check")
    seconds=input()
    if(System == "Linux"):
          
        os.system("echo The date and time is: $(date '+%d/%m/%Y %H:%M:%S') >> serviceList")
        os.system("service --status-all | grep + | cut -c9->>serviceList")    
        while True:
             
            os.system("service --status-all | grep + | cut -c9- >>linux.txt") 
            
            time.sleep(float(seconds))
            
            os.system("service --status-all | grep + | cut -c9- >>tee.txt")
            os.system("echo The date and time is: $(date '+%d/%m/%Y %H:%M:%S') >> serviceList")
            os.system("cat tee.txt>>serviceList")
            fox.dif("linux.txt", "tee.txt") 
            
            os.system("rm linux.txt")
            os.system("rm tee.txt")
            if (os.stat("different.txt") != 0):
                os.system("echo The date and time is: $(date '+%d/%m/%Y %H:%M:%S') >> Status_Log.txt")
                os.system("cat different.txt >> Status_Log.txt")
                os.system("cat different.txt")
            os.system("rm different.txt")
            signal.signal(signal.SIGINT, signal_handler)
                       
            
