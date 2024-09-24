# (c) Caleb Lazarow, 2024. All Rights reserved. Code credits are given to the proper author(s) in print.
# Failure to follow directions in the "LICENSE" file will result in an automatic deletion of your
# fork of this project. Thank you for your cooperation.

# | ------------------------------------------------------------- |
# |     A NOTE TO AP/NON AP COMPUTER SCIENCE PRINCIPLES STUDENTS: |
# |								  |
# | 	Hello there,						  |
# | 	This is my code, and it's being developed as we speak.	  |
# |								  |
# |	This is the code that I gave to my teacher and		  |
# |	got some valuable feedback. You are allowed to use	  |
# | 	this code as an example, and NOT copy directly out and	  |
# | 	claim this as your own. Feel free to explore this and	  |
# | 	find what variables are being used throughout the code.	  |
# | 								  |
# |	If you do copy the code directly, claim it as your own,	  |
# |	and not give proper claims to who created the code (me),  |
# |	I will make sure you will get a zero on this project, and |
# | 	I will make sure you will not pass the AP test with a	  |
# | 	teacher phone call to who copied my code.		  |
# | 	Thank you,						  |
# | 	Caleb Lazarow						  |
# | 	Former APCSP student					  |
# | ------------------------------------------------------------- |


# ------------------------------------------------
# Comments on what's going to happen (...or the friendly way of doing things)
# Beginning of code segments

# Imports files from pip (Python) library, if necessary
# Please use the following command to install the necessary libraries:
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
import datetime

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

# Flags/Arguments necessary to run

parser = argparse.ArgumentParser(description='DDoM - Modified for Create PT 2023-2024 Project')
parser.add_argument("-c", "--count", nargs=1, type=int, help="Defines number of malware samples you want, up to 100. If nothing is present, the arguement is set to 5 by default.",
                required=False, default=argparse.SUPPRESS, metavar="SAMPLES")             

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
    print("[*] Please note, not all samples may be downloaded.")
    scount = 5
else:
    scount = args.count[0]

if scount >= 101:
	scount = 100
	print("[*] Number of samples is over the limit, going with 100 samples...")
	print("[*] Please note, not all samples may be downloaded.")



# End of help menu
# ------------------------------------------------

# Variables / Confirmation prompts

final_list = []  # Address Collector
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
} 

print("""\nYou'll get these {} samples each from:
\t# http://vxvault.net
""".format(scount))

confirmed = confirmation("Do you affirm to start downloading these {} samples?".format(scount), "no") # Confirmation prompt #1: Are you sure you want to download these samples?
if not confirmed:
    sys.exit("[*] Thank you for using this application.")

confirmed = confirmation("Last chance! Are you sure to download these {} samples from the internet?".format(scount), "no") #Confirmation prompt #2: Last chance to download samples
if not confirmed:
    sys.exit("[*] Thank you for using this application.")

# End of Variables / Confirmation prompts
# ------------------------------------------------

# Start of downloading samples
# This portion of code was with the help of GitHub Copilot, a tool that helps with code completion.
    
# Checking location of samples folder
    
print("\n[*] Checking if Samples folder exists...")

if not os.path.exists("/Samples"):
    print("\n[*] Samples folder does not exist. Creating folder...")
    os.makedirs("/Samples")
    print("\n[*] Folder created at Samples")

else:
    print("\n[*] Samples folder already exists. Downloading samples...")

# ------------------------------------------------

# start of downloading samples
# Samples downloaded from vxvault.net

print("\n[*] Downloading samples from vxvault.net...")

# Downloads original list from vxvault.net
response = requests.get("http://vxvault.net/URL_List.php")
os.makedirs("Samples", exist_ok=True)
if response.status_code == 200:
    with open("Samples/vxvault.net_websites.html", "wb") as f:
        f.write(response.content)


# Downloads original list from vxvault.net, then downloads samples from the file provided
# Opens the file from the original list and downloads the samples from the list, up to the
# number of samples requested (i - 1, for simplicity)
# If i == scount - 1, the loop breaks and the program will stop downloading samples

if os.path.exists("Samples/vxvault.net_websites.html"):
    with open("Samples/vxvault.net_websites.html", "r") as f:
        content = f.read()
        urls = re.findall(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", content)
        i = 0
        for url in urls:
            try:
                response = requests.get(url[0], headers=headers)
                if response.status_code == 200:
                    with open("Samples/vxvault.net_{}.exe".format(i), "wb") as f:
                        f.write(response.content)
                        final_list.append("vxvault.net_{}.exe".format(i))
                        i += 1
                        if i == scount:
                            break
            except Exception as e:
                print("Error: ", e)


# end of downloading samples from vxvault.net
# ------------------------------------------------
# Final Print - Thanks for downloading samples

if(scount - 1 == i - 1):
    print("\n[*] {} sample(s) has been downloaded to your computer!".format(scount))
    print("\n[*] Samples are located in the 'Samples' folder.")
    print("\n[*] Thank you for using this program!")
else:
    print("\n[*] Error in downloading samples. Please try again later.")
    print("\n[*] Thank you for using this program!")
# End of program
