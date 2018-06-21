# Multi-agent accelerator for Data Science (acnsmauricedsmas)
This library allows users to harness the power of agent-based computing using hundreds of advanced linear and non-linear algorithms.  The system can:

    1. Automatically analyse your data and perform feature selection to determine which variables are more important than others
    2. Automatically model your data for seasonality: Winter, Shoulder, and Summer seasons
    3. Automatically clean your data for outliers
    4. Automatically make predictions using the BEST algorithm (out of hundreds) that best model your data
    5. Do all this in minutes

To install this library a request should be made to sebastian.maurice@gmail.com for a username and password.  Once you have these credentials then install this Python library.

# Installation
 ## Issue a _PIP install acnsmauricedsmas_ at the command prompt.  
 ### (This assumes you have Python installed on your computer.)

# Syntax
There are literally two lines of code you need to write to train your data and make predictions.
thedata=acnsmauricedsmas.dotraining('C:\\CORE_FILES\\Accenture\\VistraEnergy\\Models\\test2log.csv','demouser','demouser321',1,0,0,'binaward','otics','admin@analytix.ai')

**import acnsmauricedsmas**
1. acnsmauricedsmas.**dotraining**(_file, username, password, feature_analysis, remove_outliers, has_seasonality, dependent_variable, your_company_name, your_email_)

**Parameters:**	

fit_intercept : boolean, optional, default True

whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations (e.g. data is expected to be already centered).

normalize : boolean, optional, default False

This parameter is ignored when fit_intercept is set to False. If True, the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm. If you wish to standardize, please use sklearn.preprocessing.StandardScaler before calling fit on an estimator with normalize=False.

copy_X : boolean, optional, default True

If True, X will be copied; else, it may be overwritten.

n_jobs : int, optional, default 1
