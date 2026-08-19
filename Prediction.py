from data_preprocession import x_train, y_train, x_test, y_test
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

model = DecisionTreeRegressor(random_state=42)

model.fit(x_train, y_train)

machine_prediction = model.predict(x_test)
actual_result = y_test

mae = mean_absolute_error(actual_result, machine_prediction)
mse = mean_squared_error(actual_result, machine_prediction)
rmse = root_mean_squared_error(actual_result, machine_prediction)
r2 = r2_score(actual_result, machine_prediction)

print(f"The Mean absolute error is {mae}\n")
print(f"The Mean Squared error is {mse}\n")
print(f"The Root Mean absolute error is {rmse}\n")
print(f"The R2 score is {r2}")

plt.scatter(
    actual_result,
    machine_prediction,
    color="orange",
    label="Predictions"
)

plt.plot(
    [actual_result.min(), actual_result.max()],
    [actual_result.min(), actual_result.max()],
    linestyle="--",
    color="blue",
    label="Perfect Prediction"
)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.legend()

plt.show()







