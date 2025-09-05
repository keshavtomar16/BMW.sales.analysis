import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("BMW sales data (2010-2024) (1).csv")  
print(df.shape)
print(df.columns) 
print(df.info())  
print(df.head())
print(df.duplicated().sum())
df["Year"] = df["Year"].astype(int)
#sales_by_year = df.groupby("Year")["Sales_Volume"].sum()
#print(sales_by_year)
top_models = df.groupby("Model")["Sales_Volume"].sum().sort_values(ascending=False).head(5)
print(top_models)
region_sales = df.groupby("Region")["Sales_Volume"].sum()
print(region_sales)
print(df.select_dtypes(include=["int64", "float64"]).corr())
import matplotlib.pyplot as plt
sales_by_year = df.groupby("Year")["Sales_Volume"].sum()
sales_by_year.plot(kind="line", marker="o", title="BMW Sales Trend (2010-2024)")
plt.xlabel("Year")
plt.ylabel("Sales_Volume")
plt.show()
top_models = df.groupby("Model")["Sales_Volume"].sum().sort_values(ascending=False).head(5)

top_models.plot(kind="bar", title="Top 5 BMW Models by Sales")
plt.ylabel("Sales_Volume")
plt.show()
region_sales = df.groupby("Region")["Sales_Volume"].sum()

region_sales.plot(kind="pie", autopct="%1.1f%%", title="Region-wise Sales Share")
plt.ylabel("")
plt.show()

