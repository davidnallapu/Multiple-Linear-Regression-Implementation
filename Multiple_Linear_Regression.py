#Multiple Regression
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the dummy variable trap
X=X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

import statsmodels.formula.api as sm

def backwardElimination(x,sl):
    no_of_var=len(x[0])
    for i in range(0,no_of_var):
        regressor_OLS=sm.OLS(endog=y, exog= x).fit()
        maxVar=max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0,no_of_var-i):
                if(regressor_OLS.pvalues[j].astype(float)==maxVar):
                    x=np.delete(x,j,1)
    regressor_OLS.summary()
    return x                    
X=np.append(arr= np.ones((50,1)).astype(int),values= X, axis=1)                   
X_opt= X[:,[0,1,2,3,4,5]]    
X_modeled= backwardElimination(X_opt,0.05)

"""Done without Backward Elimination function
X_opt= X[:,[0,1,2,3,4,5]]
#SL=0.05
regressor_OLS=sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()
X_opt= X[:,[0,1,3,4,5]]
regressor_OLS=sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()
X_opt= X[:,[0,3,4,5]]
regressor_OLS=sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()
X_opt= X[:,[0,3,5]]
regressor_OLS=sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()
X_opt= X[:,[0,3]]
regressor_OLS=sm.OLS(endog=y, exog= X_opt).fit()
regressor_OLS.summary()
"""   
# Fitting Multiple Linear Regression to the Training set with Backward Elimination
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_opt, y, test_size = 0.2, random_state = 0)
regressor2 = LinearRegression()
regressor2.fit(X_train2, y_train2)

# Predicting the Test set results
y_pred_BL = regressor2.predict(X_test2)

#Plotting the graph

#Plotting the graph
plt.plot(y_pred_BL, color='blue')
plt.plot(y_test2, color='red')
plt.xlabel('Blue=Predicted with Backward Elimination \n Red=Test results from input Data')
plt.show()

"""The .csv file can be changed and this model can be used accordingly"""
