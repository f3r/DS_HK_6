import os
import pandas as pd
import sys 
import urllib

BASE_URL = "https://docs.google.com/forms/d/1FOGs32T-0DZSwOHE-1r8rP6m4fI3fYxSC9jmd7rd7ak/viewform?entry.902636390="
INTERFIX = "&entry.1478388549="
SUFFIX = "&entry.1994883592&entry.1985262344&entry.1394458725&entry.563048722"
emails = pd.read_csv('emails.csv', names=['address'])
classes = pd.read_csv('classes.csv', names=['topic'])
topic = classes.topic.values[int(sys.argv[1]) - 1] 

for address in emails.address.values:
	url = BASE_URL + address + INTERFIX + urllib.quote_plus(topic) + SUFFIX
 	msg = 'Please give your feedback at:\n\n' + url
 	cmd = "echo '%s' | mutt -s 'Exit Ticket' %s" % (msg, address)
	os.system(cmd)