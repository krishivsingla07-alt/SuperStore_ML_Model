Superstore Sales Prediction

A machine learning project using the Superstore dataset to predict Sales.

The project is being developed incrementally, with each version focusing on improving my understanding of the data and the machine learning workflow.

Version 1 — Basic ML Model
Objective

Predict Sales using:

Quantity
Discount
Segment
Category
Region
Preprocessing
Checked for missing values
One-hot encoded categorical variables
Split data into 80% training and 20% testing data
Model

Decision Tree Regressor

Results
Metric	Result
MAE	253.04
MSE	587071.18
RMSE	766.21
R²	0.0061
What I Learned
Difference between classification and regression
One-hot encoding
Train/test splitting
Training a regression model
Making predictions
MAE, MSE, RMSE and R²
Conclusion

The Version 1 model explains only about 0.6% of the variation in Sales.

This provided a baseline for understanding how well the initial feature set could predict Sales.

Version 2 — Data Visualization & Exploratory Analysis

Version 2 focuses on understanding the dataset before making further changes to the machine learning model.

The goal was to investigate whether the features selected in Version 1 actually show meaningful relationships with Sales.

Part 1 — Basic Visualizations
Bar Charts

Bar charts were used to compare Sales across categorical variables such as:

Category
Segment
Region
Scatter Plots

Scatter plots were used to investigate relationships between numerical variables and Sales, including:

Quantity vs Sales
Discount vs Sales
Profit vs Sales
Initial Observations

The visualizations showed that:

Category vs Sales showed a noticeable difference between categories.
Other categorical variables did not show a very strong difference in Sales.
Scatter plots helped visualize the relationships between numerical variables and Sales.
Some relationships appear weak, suggesting that simply using these features may not be sufficient for accurate Sales prediction.

These observations will be used to guide the next stage of analysis.

Part 2 — Further Data Exploration

The next stage of Version 2 focuses on using more informative visualization techniques to understand the dataset.

Planned analysis includes:

Box plots
Distribution analysis
Outlier detection
Deeper analysis of numerical variables
Better comparison of categorical variables
Investigating relationships between features

The purpose is to identify useful patterns and determine which features may contribute most to predicting Sales.

Version 2 — Conclusion

Version 2 shifted the focus from "Can I train a model?" to "Do I actually understand the data I'm training the model on?"

The initial visualizations showed that not all selected features have an obvious relationship with Sales.

This suggests that improving the model may require better feature selection and feature engineering, rather than simply changing the algorithm.