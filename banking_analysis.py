from readline import redisplay
import readline

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root")

query = "SELECT * FROM banking_case.customer"

# Execute the query and load the data into a pandas DataFrame
df = pd.read_sql(query, con=db_connection)
# Close the database connection
db_connection.close()
# Display the dataframe
print(df)
#Shape of the Dataset
print(df.shape)
# display the first few rows of the dataframe
print(df.head())
# Display the Info of the dataframe
print(df.info())
# Display the describe of the dataframe
print(df.describe())
# Check the Column Estimated income Values
print(df['Estimated Income'].value_counts())
# Create Income Category based on Estimated Income and display the value counts and plot the distribution of the Income Category
bins = [0,100000,300000,float('inf')]
labels = ['Low', 'Medium', 'High']
df['Income Category'] = pd.cut(df['Estimated Income'], bins=bins, labels=labels, right=False)
print(df['Income Category'].value_counts())
print(df['Income Category'].value_counts().plot(kind='bar'))
print(plt.show())
#Examine the distribution of the Unique Category in categorical columns
categorical_columns = df[['BRId','GenderId','IAId','Amount of Credit Cards',
                          'Nationality','Occupation','Fee Structure',
                          'Loyalty Classification','Properties Owned','Risk Weighting',
                          'Income Category']].columns
for col in categorical_columns:
    print(f"Values Counts for '{col}':") 
    print(df[col].value_counts().plot(kind='bar')) 
    import matplotlib.pyplot as plt
    print(plt.show())

#Univarite Analysis
for i,predictor in enumerate(df[['BRId','GenderId','IAId','Amount of Credit Cards',
                          'Nationality','Occupation','Fee Structure',
                          'Loyalty Classification','Properties Owned','Risk Weighting',
                          'Income Category']].columns):
    plt.figure(figsize=(10, 6))
    sns.countplot(x=predictor, data=df,hue='GenderId',palette='viridis')
    plt.show()

for i,predictor in enumerate(df[['BRId','GenderId','IAId','Amount of Credit Cards',
                          'Nationality','Occupation','Fee Structure',
                          'Loyalty Classification','Properties Owned','Risk Weighting',
                          'Income Category']].columns):
    plt.figure(figsize=(10, 6))
    sns.countplot(x=predictor, data=df,hue='Nationality',palette='pastel')
    plt.show()

# Histplot of Value counts for different Occupation
for col in categorical_columns:
    if col =='Occupation':
        continue
    plt.figure(figsize=(8,4))
    sns.histplot(df[col])
    plt.title('Histogram of Occupation Count')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()

#Numerical Analysis
numerical_cols = ['Estimated Income','Superannuation Savings','Credit Card Balance','Bank Loans','Bank Deposits','Checking Accounts','Saving Accounts','Foreign Currency Account','Business Lending']
# univariate analysis and visualization
plt.figure(figsize=(8,4))
for i, col in enumerate(numerical_cols):
    plt.subplot(4,3,i+1)
    sns.histplot(df[col],kde=True)
    plt.title(col)
plt.show()

#Heat Maps
numerical_cols = ['Estimated Income','Superannuation Savings','Credit Card Balance','Bank Loans','Bank Deposits','Checking Accounts','Saving Accounts','Foreign Currency Account','Business Lending']
correlation_matrix = df[numerical_cols].corr()
plt.figure(figsize=(10, 8)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',fmt=".2f",linewidths=0.5)
plt.show()