# Author: Manu Gupta
# BPIT- GGSIPU
# Date Created: 16/05/2016
# Last Modified: 16/05/2016 15:55hrs I.S.T
# Brute Forcing method to find Roll No. from  just Name (CSBE)
import requests
# Headers for initiating POST request to cbse site
headers = {'Origin': 'http://resultsarchives.nic.in', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36','Referer': 'http://resultsarchives.nic.in/cbseresults/cbseresults2014/class12/cbse122014_total.htm' }
# Initial roll number from where brute forcing should start
roll_no = 9201400
# For further contraints, check HTML source code of CBSE result site
name = "MANU";
# Boolean var for exiting while loop if NAME is found
flag = 0
#Variable to hold Searched ROLL NUMBER
saved_roll_no = 1234567
count = 0
while (flag == 0):
   r = requests.post("http://resultsarchives.nic.in/cbseresults/cbseresults2014/class12/cbse122014_total.htm", data={'regno': roll_no, 'B1': 'Submit'}, headers=headers)
   if r.text.find(name) == -1:
       flag = 0
   else:
        saved_roll_no = roll_no
        flag = 1
   # Un-Comment below statement if you want to see which roll numbers are already processed!
   #print roll_no    
   roll_no = roll_no + 1
print "Roll Number found for Name: " + name + ", its: "
print saved_roll_no

#Further improvments...
# Rather finding name in whole response , just find in the place where it actually should be around 2800 Position
# Applying more constraints in Brute Forcing
# This program searches first occurance of the name in the database for Exhaustive search change will condition to while( roll_no < MAX_ROLL_NO )
# or after first search change initial roll number to that saved_roll_no and re-execute the program!
# and Many More....
