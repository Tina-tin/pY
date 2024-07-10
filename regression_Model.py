import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Initialize a Linear Regression model
model =LinearRegression()

# create dataframe using pandas
data = pd.read_csv("advertising.csv")
print(data.head())

# Define the target variable (y) as 'Sales' column values
y = data['Sales'].values

# Define the feature variables (X) as 'TV', 'Radio', and 'Newspaper' columns' values
X = data[['TV','Radio','Newspaper']].values

# Fit the Linear Regression model using the feature variables (X) and target variable (y)
model.fit(X,y)

# Save the trained model using joblib
joblib.dump(model,'mymodel.csv')