#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Algorithms - Predict Solutions

# Below is the proposed model solution for the Predict deliverable of Machine Learning Algorithms. We will start by pre-processing the data.

# ## Pre-processing

# ### Import Data

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_recall_fscore_support as score

df = pd.read_csv('data.csv').drop('Unnamed: 0', axis=1)


# ### Pre-process Data

# In[2]:


# Regression labels
y_r = df['target_return']

# Classification labels
y_c = df['target_return'].apply(lambda x: 1 if x > 0 else 0)

# Features
X = df.drop(['Date', 'company', 'target_return'], axis=1)


# In[3]:


# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_standardize = pd.DataFrame(X_scaled,columns=X.columns)


# In[4]:


# Regression train/test split Test Case 1
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_standardize, y_r, test_size=0.3, random_state=101)

# Classification train/test split Test  Case 1
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_standardize, y_c, test_size=0.3, random_state=101)

# Regression train/test split Test Case 2
X_train_r2, X_test_r2, y_train_r2, y_test_r2 = train_test_split(X, y_r, test_size=0.4, random_state=100)


# ## Function 1

# Write a function to return the intercept as a float (rounded to the nearest 3 integers) of a linear regression model
# 
# * Given the training features (X_train) and labels (y_train)

# In[5]:


def lin_reg_intercept(X_train, y_train):
    
    "Returns intercept (float) of linear regression model"
    
    lnr = LinearRegression()
    lnr.fit(X_train,y_train)
    
    return round(lnr.intercept_,3)


# In[6]:


lin_reg_intercept(X_train_r, y_train_r)


# ## Function 2

# Write a function to return the number of coefficients greater than 0 in a lasso model (as an integer)
# 
# * Given the training features (X_train) and labels (y_train)
# * For a specific value of the regularisation parameter (alpha)

# In[7]:


def lasso_predictors(X_train, y_train, alpha):
    
    "Returns number (integer) of coefficients in lasso model that are greater than 0"
    
    lasso = Lasso(alpha)
    lasso.fit(X_train,y_train)
    coef = list(lasso.coef_)
    
    return len([c for c in coef if c > 0])


# In[8]:


lasso_predictors(X_train_r, y_train_r, 0.01)


# ## Function 3

# Write a function to return the mean squared error as a float (rounded to the nearest 3 integers) of a linear regression model 
# 
# * Given the training features (X_train) training labels (y_train), testing features (X_test) and testing labels (y_test)

# In[9]:


def lnr_mse(X_train, y_train, X_test, y_test):
    
    "Returns the MSE (float) of a linear regression model"
    
    # train
    lnr = LinearRegression()
    lnr.fit(X_train, y_train)
    
    # predict
    pred = lnr.predict(X_test)
    
    return round(mean_squared_error(y_test, pred),3)


# In[10]:


lnr_mse(X_train_r, y_train_r, X_test_r, y_test_r)


# ## Function 4

# Write a function to return the mean absolute error as a float (rounded to the nearest 3 integers) of a ridge regression model 
# 
# * Given the training features (X_train), training labels (y_train), testing features (X_test) and testing labels (y_test)
# * For a specific value of the regularisation parameter (alpha)

# In[11]:


def ridge_mae(X_train, y_train, X_test, y_test, alpha):
    
    "Returns the MAE (float) of the ridge regression model"
    
    # train
    ridge = Ridge(alpha)
    ridge.fit(X_train, y_train)
    
    # predict
    pred = ridge.predict(X_test)
    
    return round(mean_absolute_error(y_test, pred), 3)


# In[12]:


ridge_mae(X_train_r, y_train_r, X_test_r, y_test_r, 1)


# ## Function 5

# Write a function to return the root mean squared error as a float (rounded to the nearest 3 integers) of a linear regression model
# 
# * Given the training features (X_train), training labels (y_train), testing features (X_test) and testing labels (y_test)

# In[13]:


def lnr_rmse(X_train, y_train, X_test, y_test):
    
    "Returns the root mean squared error (float) of a linear regression model"
    
    # train
    lnr = LinearRegression()
    lnr.fit(X_train, y_train)
    
    # predict
    pred = lnr.predict(X_test)
    
    return round(np.sqrt(mean_squared_error(y_test, pred)),3)


# In[14]:


lnr_rmse(X_train_c, y_train_c, X_test_c, y_test_c)


# ## Function 6

# Write a function to return the highest coefficient in a logistic regression model as a float (rounded to the nearest 3 integers)
# 
# * Given the training features (X_train) and labels (y_train)

# In[15]:


def highest_coef(X_train, y_train):
    
    "Returns the highest coefficient in a logistic regression model as a float (rounded to the nearest 3 integers)"
    
    lgr = LogisticRegression()
    lgr.fit(X_train,y_train)
    
    return round(lgr.coef_.max(),3)


# In[16]:


highest_coef(X_train_c, y_train_c)


# ## Function 7

# Write a function to return the number of true positives (as an integer) of a logistic regression model 
# 
# * Given the training features (X_train), training labels (y_train), testing features (X_test) and testing labels (y_test)

# In[17]:


def log_reg_tp(X_train, y_train, X_test, y_test):
    
    "Returns the number (integer) of true positives for a logistic regression model"
    
    # train
    lgr = LogisticRegression()
    lgr.fit(X_train, y_train)
    
    # predict
    pred = lgr.predict(X_test)
    
    return confusion_matrix(y_test, pred)[0,0]


# In[18]:


log_reg_tp(X_train_c, y_train_c, X_test_c, y_test_c)


# ## Function 8

# Write a function to return the precision as a float (rounded to the nearest 3 integers) of a logistic regression model 
# 
# * Given the training features (X_train), training labels (y_train), testing features (X_test) and testing labels (y_test)

# In[19]:


def lgr_precision(X_train, y_train, X_test, y_test):
    
    "Returns the precision (float) for a logistic regression model"
    
    # train
    lgr = LogisticRegression()
    lgr.fit(X_train, y_train)
    
    # predict
    pred = lgr.predict(X_test)
    
    return round(score(y_test, pred, average='weighted')[0], 3)


# In[20]:


lgr_precision(X_train_c, y_train_c, X_test_c, y_test_c)


# ## Function 9

# Write a function to return the f1-score as a float (rounded to the nearest 3 integers) of a logistic regression model 
# 
# * Given the training features (X_train), training labels (y_train), testing features (X_test) and testing labels (y_test)

# In[21]:


def lgr_f1_score(X_train, y_train, X_test, y_test):
    
    "Returns the f1-score (float) for the logistic regression model"
    
    # train
    lgr = LogisticRegression()
    lgr.fit(X_train, y_train)
    
    # predict
    pred = lgr.predict(X_test)
    
    return round(score(y_test, pred, average='weighted')[2], 3)


# In[22]:


lgr_f1_score(X_train_c, y_train_c, X_test_c, y_test_c)


# ## Function 10

# Write a function to return a specific metric (precision, recall or f1-score) as a float (rounded to the nearest 3 integers) of a logistic regression model 
# 
# * Given the training features (X_train), training labels (y_train), testing features (X_test) and testing labels (y_test)

# In[23]:


def lgr_metric_output(X_train, y_train, X_test, y_test, metric):
    
    "Returns the chosen metric (float) for the logistic regression model"
    
    # train
    lgr = LogisticRegression()
    lgr.fit(X_train, y_train)
    
    # predict
    pred = lgr.predict(X_test)
    
    # metrics
    metric_dict = {'Precision':0, 'Recall':1, 'F1_score':2}
    
    return round(score(y_test, pred, average='weighted')[metric_dict[metric]], 3)


# In[24]:


lgr_metric_output(X_train_c, y_train_c, X_test_c, y_test_c, 'Precision')


# In[ ]:




