## Imports files from pip (Python) library, if necessary
# ------------------------------------------------

import argparse


# end of imports for file
# ------------------------------------------------

# Start print


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
#                  @@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@                 I recommend using Linux for downloading samples, and not
#              &@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@%             executing these on your main system... unless you know
#          %@@@@@@@@@@@,  . @@@@@@@#           @@@@@@@@ %  ,@@@@@@@@@@@(         what you're doing.
#         @@@@@@@(        @@@@ &@@@@@         @@@@@( @@@@        (@@@@@@@        
#         @@@@            @@@@     @  *     &  @     @@@@            @@@@        Thank you in advance!
#         @@@             @@@@      @@@@   @@@@      @@@@             @@@        
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
parser.add_argument("-c", "--count", nargs=1, type=int, help="Defines the number of malware samples you want, up to 5000. If the argument is omitted, sets to 10 by default.",
                required=False, default=argparse.SUPPRESS, metavar="SAMPLES")
parser.add_argument("-r", "--rename", help="[Not recommended] Makes the samples executable. Don't use this unless you're confident you won't execute them on your host.",
                required=False, action="store_const", const=True)              
parser.add_argument("-y", "--yes-to-all", help="Skips the confirmation prompt.",
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


# Original samples were counted to 100; I cut it down to 10 for convenience. There shouldn't be 100 samples on computers anyway.

args = parser.parse_args()
print(args)
if not "count" in args:
    print("[*]  Argument was omitted - going with 10 samples by default")
    scount = 10
else:
    scount = args.count[0]

# End of help menu
# ------------------------------------------------
