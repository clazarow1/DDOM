# Imports files from pip (Python) library, if necessary
# Please use the follwing command to install the necessary libraries:
# "pip install -r requirements.txt"
# ------------------------------------------------

import sys
import re 
import urllib.request
import urllib.error
import urllib.parse
import random 
import hashlib 
import requests 
import os
import argparse
import pyvirtualdisplay
from selenium import webdriver
import datetime


timestamp_now = datetime.datetime.now().strftime('%m-%d-%Y')



# end of imports for file
# ------------------------------------------------

# Start print
# Original Image link: https://www.pngwing.com/en/free-png-yxvjl

print("""\n
# Original author: https://github.com/notnop
# Original Modifier for the project: Endermanch (https://github.com/Endermanch/MalwareDatabase/blob/master/ddom.py)
# Originally modified for Python 3
# This project is inspired by Endermanch, check him out here:
# https://youtube.com/endermanch
#
#
#                                                                                
#                                  @@         @&                                 
#                              @@@               @@@                             
#                         ,@@@@@                   @@@@@.                        
#                       @@@@@                        .@@@@#                      
#                       @@@@@,                       /@@@@@                      
#                       @@@@@@                       @@@@@@                      Malware Samples downloaded to your computer!
#                       @@@@@@          /@,          @@@@@@                      
#                       @@@@@@      @@@@@@@@@@@      @@@@@@                      Please take responsibility when downloading these samples,
#                       @@@@@@# @@@@@@@.   (@@@@@@@ @@@@@@@                      as these samples can damage your host system.
#                      @@@@@@@@@@@               @@@@@@@@@@@                     
#                  @@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@                 I am not responsible for any damage caused by these samples.
#              &@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@%             Any damage caused by these samples is your at your own risk
#          %@@@@@@@@@@@,  . @@@@@@@#           @@@@@@@@ %  ,@@@@@@@@@@@(         and may lead to permanent damage to your host system, making
#         @@@@@@@(        @@@@ &@@@@@         @@@@@( @@@@        (@@@@@@@        you to reinstall your main Operating System.
#         @@@@            @@@@     @  *     &  @     @@@@            @@@@        
#         @@@             @@@@      @@@@   @@@@      @@@@             @@@        Thank you and have a great day!
#         @@              @@@@@%    @@@@@#@@@@@    @@@@@@             .@@        
#         @&                %@@@@@@*#@@@@@@@@@ @@@@@@@(                @@        
#         @                     .@@@ @@@@@@@@@ @@@                      @        
#                                    @@@@@@@@@                                   
#                                %@@@@@@@@@@@@@@@,                               
#             @.              @@@@@@@@@@@@@@@@@@@@@@@              *@            
#                 %@@@@@& ,@@@@@@@@@@        ,@@@@@@@@@@ .@@@@@@(                
#                      @@@@@@@@@*                 #@@@@@@@@@                     
#                          &                           &                       \n""")


# ------------------------------------------------
# end of print
# ------------------------------------------------

# Flags/Arguements necessary to run

parser = argparse.ArgumentParser(description='DDoM - Modified for Create PT 2023-2024 Project')
parser.add_argument("-c", "--count", nargs=1, type=int, help="Defines number of malware samples you want, up to 5000. If nothing is present, the arguement is set to 5 by default.",
                required=False, default=argparse.SUPPRESS, metavar="SAMPLES")
parser.add_argument("-r", "--rename", help="[NOT RECOMMENDED] Makes the samples executable. Don't use this unless you're confident you won't execute them on your host.",
                required=False, action="store_const", const=True)              

def confirmation(question, default="no"):    
    valid = {"yes": True, "y": True, "ye": True,
                "no": False, "n": False} 
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    validInputEntered = False
    while not validInputEntered:
        data = input("{}{}".format(question, prompt)).lower()
        if data in valid:
            validInputEntered = True
            return valid[data]
        if data == "":
            validInputEntered = True
            return default


# Original samples were counted to 100; I cut it down to 5 for convenience. There shouldn't be 100 samples on computers anyway.

args = parser.parse_args()
print(args)
if not "count" in args:
    print("[*]  Argument was omitted - going with 5 samples by default")
    scount = 5
else:
    scount = args.count[0]

# End of help menu
# ------------------------------------------------

# Variables / Confirmation prompts

final_list = []  # Address Collector
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
} 

print("""\nYou'll get these {} samples each from:
\t# https://bazaar.abuse.ch/
\t# http://vxvault.net
\t# http://tracker.h3x.eu
""".format(scount))

confirmed = confirmation("Do you affirm to start downloading these {} samples?".format(scount), "no") # Confirmation prompt #1: Are you sure you want to download these samples?
if not confirmed:
    sys.exit(0)

confirmed = confirmation("Last chance! Are you sure to download these {} samples from the internet?".format(scount), "no") #Confirmation prompt #2: Last chance to download samples
if not confirmed:
    sys.exit(0)

# End of Variables / Confirmation prompts
# ------------------------------------------------

# Start of downloading samples
# This portion of code was with the help of GitHub Copilot, a tool that helps with code completion.
    
# Checking location of samples folder
    
if not os.path.exists("/Samples"):
    print("\n[*] Samples folder does not exist. Creating folder...")
    os.makedirs("/Samples")
    print("\n[*] Folder created at /Samples")

else:
    print("\n[*] Samples folder already exists. Downloading samples...")

# ------------------------------------------------
# Samples downloaded from bazaar.abuse.ch
    
print("\n[*] Downloading samples...")
print("\n[*] Downloading samples from bazaar.abuse.ch...")
for i in range(scount):
    try:
        url = "https://bazaar.abuse.ch/browse/{}".format(random.randint(1, 5000))
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open("Samples/bazaar.abuse.ch_{}.zip".format(i), "wb") as f:
                f.write(response.content)
                final_list.append("bazaar.abuse.ch_{}.zip".format(i))
    except Exception as e:
        print("Error: ", e)

# Samples downloaded from vxvault.net
print("\n[*] Downloading samples from vxvault.net...")
for i in range(scount):
    try:
        url = "http://vxvault.net/URL_List.php"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open("Samples/vxvault.net_{}.zip".format(i), "wb") as f:
                f.write(response.content)
                final_list.append("vxvault.net_{}.zip".format(i))
    except Exception as e:
        print("Error: ", e)

# Samples downloaded from tracker.h3x.eu

print("\n[*] Downloading samples from tracker.h3x.eu...")
for i in range(scount):
    try:
        url = "http://tracker.h3x.eu/URL_List.php"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open("Samples/tracker.h3x.eu_{}.zip".format(i), "wb") as f:
                f.write(response.content)
                final_list.append("tracker.h3x.eu_{}.zip".format(i))
    except Exception as e:
        print("Error: ", e)
# end of downloading samples
# ------------------------------------------------
# start of renaming samples

if "rename" in args:
    print("\n[*] Renaming samples...")
    for i in final_list:
        try:
            os.rename("Samples/{}".format(i), "Samples/{}.exe".format(i))
        except Exception as e:
            print("Error: ", e)
# end of renaming samples
# ------------------------------------------------
# Final Print - Thanks for downloading samples

if(scount == i):
    print("\n[*] {} sample(s) has been downloaded to your computer!".format(scount))
    print("\n[*] Samples are located in the 'Samples' folder.")
    print("\n[*] Thank you for using this program!")
else:
    print("\n[*] Error in downloading samples. Please try again later.")
    print("\n[*] Thank you for using this program!")
