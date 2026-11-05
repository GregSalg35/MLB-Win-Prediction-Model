import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


df = pd.read_csv("BattingFinalData.csv")

# create the model
model = LinearRegression()

# choose data to test in model
X = df[["RperGame", "RAperGame"]]

# choose what to predict with model
y = df["W"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the model with given data
model.fit(X_train, y_train)

predictions = model.predict(X_test)

# get r^2, mean absolute error, and mean squared error using model predictions
r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)

print(model.coef_)
print(model.intercept_)

print(f"R²:   {r2:.3f}")
print(f"MAE:  {mae:.2f} wins")
print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f} wins")

slope, intercept = np.polyfit(predictions, y_test, 1)
xs = np.linspace(predictions.min(), predictions.max(), 100)
plt.plot(xs, slope * xs + intercept, color="#ec6453", label="Best fit")

plt.scatter(predictions, y_test, alpha= 0.3, color="black")
plt.xlabel("Predicted Wins")
plt.ylabel("Actual Wins")
plt.title("Predicted vs. Actual Wins From Runs Scored and Allowed per Game")
plt.grid(True)
plt.savefig("predicted_vs_actual_wins.png", dpi=150)
plt.show()