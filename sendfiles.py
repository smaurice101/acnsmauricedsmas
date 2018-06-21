#############################################################
#
#  Author: Sebastian Maurice, PhD
#  Copyright by Sebastian Maurice 2018
#  All rights reserved.
#  Email: Sebastian.maurice@gmail.com
#
#############################################################

import json, urllib
import requests
import csv
import os
import imp
import re


def returndata(buffer,label):
      if label=='PKEY:':
         val=""
         pattern = re.compile('\s*[,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         val=[s for s in listvalues if label in s]      
         rval=val[0].split(':')[1]
      elif label=='DATA:':
         val=""
         pattern = re.compile('\s*[:,\n]\s*')
         fixed = pattern.sub(', ', buffer)
         listvalues=fixed.split(', ')
         #print(listvalues)
         fdate=listvalues[1]
         inp=listvalues[2]
         pred=float(listvalues[3])
         acc=float(listvalues[4])
         rval=[fdate,inp,pred,acc]
          
      return rval

def uploadcsvfortraining(thefile,username,passw,autofeature,removeoutliers,hasseasonality,dependentvariable,company,email):

   rn=0
   tstr=''
   url='http://www.analytix.ai/stocks/otics/remotemasstream.php'
   with open(thefile, 'r') as f:
     reader = csv.reader(f)
     for row in reader:
       row = ",".join(row)
       tstr = tstr + str(row) + '\n'
       rn=rn+1
       
   head, fname = os.path.split(thefile)
   print("Please wait...training can take several minutes.")
   
   files = {'file': tstr,
    'mode':0,        
    'type':'CSV',
    'filename':fname,
    'username': username,
    'password': passw,
    'rowcount': rn,
    'autofeature': autofeature,
    'removeoutliers': removeoutliers,
    'hasseasonality': hasseasonality,
    'company': company,
    'email': email,            
    'dependentvariable': dependentvariable,
    'title':'File Upload for Training'
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg

def getpredictions(attr,pkey,thefile,username,passw,company,email):

   rn=0
   tstr=''
   url='http://www.analytix.ai/stocks/otics/remotemasstream.php'
   
   if attr==0:
      tstr=thefile
         
      files = {'file': tstr,
        'mode':1,        
        'type':'CSV',
        'pkey':pkey,            
        'username': username,
        'password': passw,
    #'rowcount': rn,
    #'autofeature': autofeature,
    #'removeoutliers': removeoutliers,
    #'hasseasonality': hasseasonality,
       'company': company,
       'email': email,            
    #'dependentvariable': dependentvariable,
       'title':'Do Predictions'
      }

   #print(files)
      r = requests.post(url, files)
      msg = r.text
   #print ("Message %s" % (msg))
   
      return msg


def dolistkeys(username,passw,company,email):

   rn=0
   tstr=''
   url='http://www.analytix.ai/stocks/otics/remotemasstream.php'
   
   files = {
      'mode':2,        
      'type':'CSV',        
      'username': username,
      'password': passw,
      'company': company,
      'email': email,              
     'title':'Do List keys'
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg

def dolistkeyswithkey(username,passw,company,email,pkey):

   rn=0
   tstr=''
   url='http://www.analytix.ai/stocks/otics/remotemasstream.php'
   
   files = {
      'mode':3,
      'pkey':pkey,        
      'type':'CSV',        
      'username': username,
      'password': passw,
      'company': company,
      'email': email,              
     'title':'Do List keys with Key'
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg

def dodeletewithkey(username,passw,company,email,pkey):

   rn=0
   tstr=''
   url='http://www.analytix.ai/stocks/otics/remotemasstream.php'
   
   files = {
      'mode':4,
      'pkey':pkey,        
      'type':'CSV',        
      'username': username,
      'password': passw,
      'company': company,
      'email': email,              
     'title':'Do Delete with Key'
   }

   #print(files)
   r = requests.post(url, files)
   msg = r.text
   #print ("Message %s" % (msg))
   
   return msg
