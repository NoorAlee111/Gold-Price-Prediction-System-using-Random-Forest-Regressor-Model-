#Importing the Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# loading the csv data to a Pandas DataFrame
gold_data = pd.read_csv('content/gld_price_data.csv')

#print first 5 rows in the dataframe


gold_data.head()

# print last 5 rows in the dataframe
gold_data.tail()
# number of rows and columns
gold_data.shape

# getting some basic informations about the data
gold_data.info()

# getting the statistical measures of the data
gold_data.describe()
#Correlation:1 Positive Correlation 2 Negative Correlation

# Drop the non-numeric 'Date' column for correlation computation
correlation = gold_data.drop(columns=['Date']).corr()

# Constructing a heatmap to understand the correlation
plt.figure(figsize=(6, 6))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 6}, cmap='Blues')

# Correlation values of GLD
print(correlation['GLD'])

# checking the distribution of the GLD Price
sns.displot(gold_data['GLD'], kde=True, color='green')
#sns.distplot(gold_data['GLD'], kde=True, color='green')

#Splitting the Features and Target
X = gold_data.drop(['Date','GLD'],axis=1)
Y = gold_data['GLD']

print(X)
print(Y)
#Splitting into Training data and Test Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=2)

#Model Training: Random Forest Regressor
regressor = RandomForestRegressor(n_estimators=100)
# training the model
regressor.fit(X_train,Y_train)

# prediction on Test Data
test_data_prediction = regressor.predict(X_test)
print(test_data_prediction)
# R squared error
error_score = metrics.r2_score(Y_test, test_data_prediction)
print("R squared error : ", error_score)

#Compare the Actual Values and Predicted Values in a Plot
Y_test = list(Y_test)
plt.figure() 
plt.plot(Y_test, color='blue', label = 'Actual Value')
plt.plot(test_data_prediction, color='green', label='Predicted Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('GLD Price')
plt.legend()
plt.show()


