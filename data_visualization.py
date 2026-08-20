from data_preprocession import copy, y
import matplotlib.pyplot as plt
import pandas as pd

new = copy[["Quantity", "Discount", "Segment", "Category", "Region"]]

# #relationship between Categories and sales
category_result = copy.groupby("Category")["Sales"].mean()
plt.bar(category_result.index, category_result.values)
plt.xlabel("Category")
plt.ylabel("Sales")
# plt.show()


region_sales = copy.groupby("Region")["Sales"].mean()

plt.bar(region_sales.index, region_sales.values)

plt.title("Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Sales")

# plt.show()

#Box Plot between Category and sales
categorical_sales = copy["Category"].unique()
cateforical = []

for category in categorical_sales:
    sales_c = copy[copy["Category"] == category]["Sales"]
    cateforical.append(sales_c)

plt.boxplot(cateforical)
plt.title("Categorical Sales")
plt.xticks(range(1,len(categorical_sales)+1), categorical_sales)
plt.grid()
# plt.show()

#Now to find correlation

correlation = copy[["Quantity", "Discount", "Sales"]].corr()
print(correlation)

plt.imshow(correlation)
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.title("Correlation Heatmap")

plt.show()

#scatter between month and sales
monthly = copy.groupby("Month")["Sales"].sum()
plt.bar(monthly.index, monthly.values)
plt.title("Monthly Sales")
plt.show()

#monthly+yearly

yearly_monthly = copy.groupby("Days")["Sales"].mean()
yearly_monthly.plot(kind="line")
plt.show()


plt.plot(copy["Sales"])
plt.show()

