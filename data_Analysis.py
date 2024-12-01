import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('data.xlsx')

# Convert 'price' and 'sales_price' to numeric, forcing errors to NaN 
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['sales_price'] = pd.to_numeric(df['sales_price'], errors='coerce')

# a. Most expensive product
most_expensive = df.loc[df['sales_price'].idxmax()]

# b. Cheapest product
cheapest = df.loc[df['sales_price'].idxmin()]

# c. Number of Products from Each brand
brand_counts = df['brand'].value_counts()

# d. Number of Products by Seller (Sponsored vs Non-Sponsored)
sponsored_counts = df['sponsored'].value_counts()

# Visualizing the data 


plt.figure(figsize=(14, 10))

# Plot 1: Most expensive and cheapest products
plt.subplot(2, 2, 1)
plt.bar(['Most Expensive', 'Cheapest'], [most_expensive['sales_price'], cheapest['sales_price']])
plt.title('Most Expensive vs Cheapest Product')
plt.ylabel('Price')

# Plot 2: Number of Products by Brand
plt.subplot(2, 2, 2)
brand_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Products from Each Brand')
plt.xlabel('Brand')
plt.ylabel('Number of Products')
plt.xticks(rotation=90)

# Plot 3: Number of Products by Seller (Sponsored vs Non-Sponsored)
plt.subplot(2, 2, 3)
sponsored_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
plt.title('Product Distribution by Seller (Sponsored vs Non-Sponsored)')
plt.ylabel('')  

# Plot 4: Sales Price Distribution (Optional - example of additional chart)
plt.subplot(2, 2, 4)
df['sales_price'].dropna().hist(bins=20, color='lightblue', edgecolor='black')
plt.title('Sales Price Distribution')
plt.xlabel('Price')
plt.ylabel('Frequency')

# Display all the charts
plt.tight_layout()
plt.show()



