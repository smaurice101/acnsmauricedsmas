# Multi-Agent Accelerator for Data Science (MAADS)

## Overview
This library allows users to harness the power of agent-based computing using hundreds of advanced linear and non-linear algorithms. Users can easily integrate Predictive Analytics in any solution y wrapping additional code around the functions below. The system can:

    1. Automatically analyse your data and perform feature selection to determine which variables are more 
       important than others
    2. Automatically model your data for seasonality: Winter, Shoulder, and Summer seasons
    3. Automatically clean your data for outliers
    4. Automatically make predictions using the BEST algorithm (out of hundreds of advanced algorithms) that 
       best model your data
    5. Do all this in minutes

To install this library a request should be made to the system administrator **_sebastian.maurice@gmail.com_** for a username and password.  Once you have these credentials then install this Python library.

### Compatibility
    - Python 3.5 or greater
    - Minimal Python skills needed

### License
##### Author: Sebastian Maurice, PhD
###### Copyright Sebastian Maurice (2018)
##### Free for personal use.  Commercial users please contact Sebastian Maurice.

# Installation
 ## Issue a 
 
 >pip install acnsmauricedsmas
 
 at the command prompt.  
 
 #### (This assumes you have Python installed on your computer and latest version of PIP.) [a Link](https://www.python.org/downloads/)

# Syntax
There are literally two lines of code you need to write to train your data and make predictions:

#### Main functions:

- **_dotraining_**
       - Executes hundreds of agents, running hundreds of advanced algorithms.  A master agent then chooses the BEST algorithm that best          models your data.
- **_dopredictions_**
       - After training, make high quality predictions.

#### Support functions:

- **_dolistkeys_**
        - List all of the keys associated with the data you have analysed. 
- **_dolistkeyswithkey_**
        - List data associated with a single key.
- **_dodeletewithkey_**
        - Permanently delete all data associated with your key.

### First import the Python library.

>**_import acnsmauricedsmas_**

##### 1. acnsmauricedsmas.**dotraining**(_CSV_local_file, username, password, feature_analysis, remove_outliers, has_seasonality, dependent_variable, your_company_name, your_email_)

**Parameters:**	

_CSV_local_file_ : string, required

     A local comma-separated-file (csv) with Date in the first column.  Date must be MM/DD/YYYY format.  
     All other data must be numbers.

_username_ : string, required
     
     A username issued by the system administrator. 

_password_ : string, required 

     A password issued by the system administrator.

_feature_analysis_ : int, required, 1 or 0

    If 1, then a feature analysis will be done on your file.  If 0, no analysis is done.
    
_remove_outliers_ : int, required, 1 or 0

    If 1, then outliers will be removed from your data.  If 0, no outliers are removed.

_has_seasonality_ : int, required, 1 or 0
      
       If 1, then your data will be modeled for seasonality: Winter, Summer, Shoulder. If 0, then your data will 
       not be modeled for seasonality.  If modeling for seasonality, ensure you have enough data points that 
       covers the seasons, usually 1 year of data.

_dependent_variable_ : string, required
       
       This is the dependent variable in your file.  All other variables will be modeled as independent variables.
       
_your_company_name_ : string, required

       Indicate your company name, the one associated with your username. 
       
_your_email_ : string, required       
        
       Indicate your email, the one associated with your username. 

   **Returns:** string buffer
        
        The string buffer contains the following sections:
        
            DATA: : This consists of the feature selection results
            PKEY: : This is the key to the BEST algorithm and must be used when making predictions.
        

#### 2. acnsmauricedsmas.**dopredictions**(_attr,pkey,inputs,username,password,your_company_name, your_email_)

**Parameters:**	

_attr_ : int, required

     This value should be 0.  It may change to other values in the future.

_pkey_ : string, required

     This value must be retrieved from dotraining.  Note you can store PKEY after you have trained your file. 
     Training does not have to run before predictions, as training occurs more infrequently.

_inputs_ : string, required
     
     This is a row of input data that must match the independent variables in your CSV. For example, if your 
     trained file is: Date, A, B, C, D and A is your dependent variable, then your inputs must be:
     Date, B, C, D

_username_ : string, required
     
     A username issued by the system administrator. 

_password_ : string, required 

     A password issued by the system administrator.
     
_your_company_name_ : string, required

       Indicate your company name, the one associated with your username. 
       
_your_email_ : string, required       
        
       Indicate your email, the one associated with your username. 
     
   **Returns:** string buffer
        
        The string buffer contains the following sections:
        
            DATA: : This contains your prediction.

#### 3. acnsmauricedsmas.**returndata**(_thepredictions, section_attr_)

**Parameters:**	

_thepredictions_ : string buffer

     This value is returned from dopredictions.

_section_attr_ : string buffer

     This value can be one of two values:
        
        PKEY: : This returns the key from the dotraining function.  Note the semi-colon.
        DATA: : This returns the data from the dotraining or dopredictions functions.  Note the semi-colon.
        
        
   **Returns:** string buffer
        
        The string buffer contains the prediction or the key or the feature analysis.
        
#### 4. acnsmauricedsmas.**dodeletewithkey**(_username,password,company,email,pkey_)

**Parameters:**	

_username_ : string buffer

     The username given to you by system administrator.

_password_ : string buffer

     The password given to you by system administrator.

_company_ : string buffer

     Your company assicated with your username.

_email_ : string buffer

     Your email associated with your username.

_pkey_ : string buffer

     The key you want deleted.  This can be attained from dolistkeys function.

   **Returns:** NULL
        
        Deletes all files and tables associated with the key permanently.
        
#### 5. acnsmauricedsmas.**dolistkeys**(_username,password,company,email_)

**Parameters:**	

_username_ : string buffer

     The username given to you by system administrator.

_password_ : string buffer

     The password given to you by system administrator.

_company_ : string buffer

     Your company assicated with your username.

_email_ : string buffer

     Your email associated with your username.

   **Returns:** string buffer
        
        Lists all the keys associated with your username.
        
#### 6. acnsmauricedsmas.**dolistkeyswithkey**(_username,password,company,email, pkey_)

**Parameters:**	

_username_ : string buffer

     The username given to you by system administrator.

_password_ : string buffer

     The password given to you by system administrator.

_company_ : string buffer

     Your company assicated with your username.

_email_ : string buffer

     Your email associated with your username.

_pkey_ : string buffer

     The key you want returned.

   **Returns:** string buffer
        
        Returns the information (with independent variables) associated with your key.
        
            
            
        
