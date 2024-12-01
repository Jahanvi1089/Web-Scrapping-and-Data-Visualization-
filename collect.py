#I have stored the extracted data in Excel instead of CSV for better formatting 
from bs4 import BeautifulSoup
import os
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook # type: ignore

# Initialize the data dictionary
d = {
    'current_date_time': [],
    'product_link': [],
    'product_name': [],
    'brand': [],
    'sponsored': [],
    'price': [],
    'sales_price': [],
    'express': [],
    'discount': []
}

# Process each file in the "data" directory
for file in os.listdir("data"):
    try:
        # Read the HTML file
        with open(f"data/{file}", encoding='utf-8') as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Extract fields
        current_date_time = datetime.now().strftime("%d-%m-%Y")



        # Product ID 
        product_link_tag = soup.find('a', {'id': lambda x: x and x.startswith('productBox-')})
        product_link = "https://www.noon.com/" + product_link_tag['href'] if product_link_tag else "N/A"
        
        # Product Name
        product_name_div = soup.find('div', {'data-qa': 'product-name'})
        product_name = product_name_div['title'] if product_name_div else "N/A"
        
        # Brand
        brand = product_name.split()[0] if product_name != "N/A" else "N/A"
        
        # Sponsored
        sponsored_tag = soup.find('div', class_='gzboVs')
        sponsored = 'Y' if sponsored_tag and 'Sponsored' in sponsored_tag.get_text() else 'N'
        
        # Price
        price_span = soup.find('span', class_='oldPrice')
        price = price_span.get_text(strip=True).replace('<!-- -->', '') if price_span else "N/A"
        
        # Sales Price
        sales_price_strong = soup.find('strong', class_='amount')
        sales_price = sales_price_strong.get_text(strip=True) if sales_price_strong else "N/A"
        
        # Express
        express_div = soup.find('div', {'data-qa': 'product-noon-express'})
        express = 'Y' if express_div else "N"
        
        # Discount
        discount_span = soup.find('span', class_='discount')
        discount = discount_span.get_text(strip=True) if discount_span else "N/A"
        
        # Append to dictionary
        d['current_date_time'].append(current_date_time)
        d['product_link'].append(product_link)
        d['product_name'].append(product_name)
        d['brand'].append(brand)
        d['sponsored'].append(sponsored)
        d['price'].append(price)
        d['sales_price'].append(sales_price)
        d['express'].append(express)
        d['discount'].append(discount)
    
    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Convert dictionary to DataFrame
df = pd.DataFrame(data=d)

output_file = "data.xlsx"
df.to_excel(output_file, index=False)  # Save as Excel file
print(f"Data saved to {output_file}")
