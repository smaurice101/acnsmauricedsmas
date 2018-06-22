#############################################################
#
#  Author: Sebastian Maurice, PhD                           #
#  Copyright by Sebastian Maurice 2018                      #
#  All rights reserved.
#  Email: Sebastian.maurice@gmail.com
#
#############################################################

import imp


maspredictions = imp.load_source('maspredictions','sendfiles.py')

    
def dotraining(thefile,username,passw,autofeature,removeoutliers,hasseasonality,dependentvariable,company,email):
   rmsg=maspredictions.uploadcsvfortraining(thefile,username,passw,autofeature,removeoutliers,hasseasonality,dependentvariable,company,email)
   #print(rmsg)
   return rmsg

def dopredictions(attr,pkey,thefile,username,passw,company,email):
   rmsg=maspredictions.getpredictions(attr,pkey,thefile,username,passw,company,email)
   #print(rmsg)
   return rmsg

