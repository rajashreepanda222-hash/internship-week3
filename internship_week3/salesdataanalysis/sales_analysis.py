import pandas as pd

# Day1
df = pd.read_csv("sales_data.csv")

# Display first rows
print(df.head())


# Day2
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)


print("\nData Types:")
print(df.dtypes)

print("\nDataset Info:")
print(df.info())


#Day3

print("\nMissing Values:")
print(df.isnull().sum())

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())


df["Price"] = df["Price"].fillna(df["Price"].mean())

df = df.drop_duplicates()

print("\nData After Cleaning:")
print(df)

#Day4

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nDataset with Total Sales:")
print(df)

total_revenue = df["Total_Sales"].sum()

print("\nTotal Revenue:")
print(f"₹{total_revenue:,.2f}")

best_product = df.groupby("Product")["Quantity"].sum()

print("\nProduct Sales:")
print(best_product)

print("\nBest Selling Product:")
print(best_product.idxmax())

average_sales = df["Total_Sales"].mean()


highest_sale = df["Total_Sales"].max()

lowest_sale = df["Total_Sales"].min()

print("\nAverage Sale:")
print(f"₹{average_sales:,.2f}")

print("\nHighest Sale:")
print(f"₹{highest_sale:,.2f}")

print("\nLowest Sale:")
print(f"₹{lowest_sale:,.2f}")



#Day5


print(f"\nBest Selling Product: {best_product}")
print("\nProduct-wise Quantity Sold:")
product_sales = df.groupby("Product")["Quantity"].sum()

best_product = product_sales.idxmax()
print(product_sales)