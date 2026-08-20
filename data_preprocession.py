import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

ex = pd.read_excel("data/SampleSuperstore.xlsx")

# Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
#        'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',
#        'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
#        'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'],
#       dtype='str')

#We have to predict sales based on different features
#We can use, Quantity, Discount, Segment, Category, Region

number = ex.isnull().sum().sum()
#There are no missing values in the table so we do not need to handle them



#2)Encoding Segment, Category, Region (One-hot encoding) 
copy = ex.copy()

date_time =  pd.to_datetime(copy["Order Date"])
copy["Year"] = date_time.dt.year
copy["Date"] = date_time.dt.date
copy["Month"] = date_time.dt.month
copy["Quarter"] = date_time.dt.quarter
copy["Days"] = date_time.dt.day_of_week

print(copy["Year"].head())

required = copy[['Month','Year', 'Ship Mode',
       'Segment', 'Country', 'Profit',
       'Postal Code', 'Region', 'Category', 'Sub-Category',
       'Quantity', 'Discount']]
One_hot = pd.get_dummies(required, columns=["Segment", "Category", "Region", "Sub-Category", 
                                            "Ship Mode", "Country"])
y = copy[["Sales"]]
# print(One_hot.columns)

#Splitting data
x_train, x_test, y_train, y_test = train_test_split(One_hot, y, test_size=0.2, random_state=42)


# One_hot.to_excel(r"C:\Users\Krishiv\Desktop\Training_test.xlsx", index=False)

print(One_hot.columns)



