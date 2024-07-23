from sqlalchemy import create_engine
import pandas as pd

# Database connection parameters
username = 'postgres'
password = 'Khush@2001'
host = 'localhost'
port = '5432'
database = 'mydb'

# Create an engine instance
engine = create_engine(f'postgresql://{username}:{password}@{host}:{port}/{database}')

# Query to get the data
query = "SELECT * FROM superstore_sales;"

# Load data into a pandas DataFrame
df = pd.read_sql(query, engine)


print(df.head())

'''Cleaning and Pre-processing the data'''

# Convert date columns to datetime format
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])

# Extract features from date columns
df['Order_Year'] = df['Order_Date'].dt.year
df['Order_Month'] = df['Order_Date'].dt.month
df['Order_Quarter'] = df['Order_Date'].dt.quarter

# Handle missing values if any
df.fillna(0, inplace=True)

print(df.head())

'''Feature Engineering'''
df['Days_to_Ship'] = (df['Ship_Date'] - df['Order_Date']).dt.days
monthly_sales = df.groupby(['Order_Year', 'Order_Month'])['Sales'].sum().reset_index()
monthly_sales.columns = ['Year', 'Month', 'Total_Sales']

print(monthly_sales.head())

'''Modelling'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = monthly_sales[['Year','Month']]
y = monthly_sales['Total_Sales']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)

print(f'Mean Squared Error: {mse}')

'''Model Evaluation'''
import numpy as np

# Calculate Root Mean Squared Error
rmse = np.sqrt(mse)
print(f'Root Mean Squared Error: {rmse}')

# Compare predicted vs actual sales
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison.head())


