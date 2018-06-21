# Multi-agent accelerator for Data Science (acnsmauricedsmas)
This library allows users to harness the power of agent-based computing using hundreds of advanced linear and non-linear algorithms.  The system can:

    1. Automatically analyse your data and perform feature selection to determine which variables are more 
    important than others
    2. Automatically model your data for seasonality: Winter, Shoulder, and Summer seasons
    3. Automatically clean your data for outliers
    4. Automatically make predictions using the BEST algorithm (out of hundreds) that best model your data
    5. Do all this in minutes

To install this library a request should be made to the system administrator **_sebastian.maurice@gmail.com_** for a username and password.  Once you have these credentials then install this Python library.

# Installation
 ## Issue a _PIP install acnsmauricedsmas_ at the command prompt.  
 ### (This assumes you have Python installed on your computer.)

# Syntax
There are literally two lines of code you need to write to train your data and make predictions.

**_import acnsmauricedsmas_**
1. acnsmauricedsmas.**dotraining**(_CSV_local_file, username, password, feature_analysis, remove_outliers, has_seasonality, dependent_variable, your_company_name, your_email_)

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

    **Returns:**
        
        

