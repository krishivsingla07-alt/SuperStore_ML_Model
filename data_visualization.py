from data_preprocession import copy, y
import matplotlib.pyplot as plt
import pandas as pd

new = copy[["Quantity", "Discount", "Segment", "Category", "Region"]]

#relationship between Quantity and sales
plt.scatter(new[["Quantity"]], y, color = "orange", label = "Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.legend()
plt.show()


# # #relationship between Discount and sales
plt.scatter(new[["Discount"]], y, color = "blue")
plt.title("Discount vs Sales")
plt.xlabel("Discount in %")
plt.ylabel("Sales")
plt.show()

# #relationship between Segment and sales (categorical: Bar)
segemtn_result = copy.groupby("Segment")["Sales"].mean()
plt.bar(segemtn_result.index, segemtn_result.values)
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.show()

#relationship between Categories and sales
category_result = copy.groupby("Category")["Sales"].mean()
plt.bar(category_result.index, category_result.values)
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


region_sales = copy.groupby("Region")["Sales"].mean()

plt.bar(region_sales.index, region_sales.values)

plt.title("Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Sales")

plt.show()

#this is all giving average values of each category, so we can use boxplot to check how it actually does these things