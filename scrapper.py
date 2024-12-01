import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Selenium with ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path='chromedriver.exe')  # Path to chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Initialize global variables
file_counter = 0  # To track the number of files saved
query = "yoga_products"  # Query name used for file naming
products = []  # List to store product data

# Create the data folder 
if not os.path.exists("data"):
    os.makedirs("data")

def scrape_noon_products():
    global file_counter  # Access the global file counter

    url = "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"
    driver.get(url)
    time.sleep(3)

    while len(products) < 200:  # Continue scrolling until 200 products are scraped
        # Scroll to the bottom to load more products
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        items = driver.find_elements(By.CLASS_NAME, "sc-980f39e6-0.iNoaVH.wrapper.productContainer")  # Adjusted class selector
        for item in items:
            html_content = item.get_attribute("outerHTML")
            products.append(html_content)  # Save product data in the list

            # Save the HTML content to a file
            with open(f"data/{query}_{file_counter}.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            file_counter += 1

            # Stop when 200 products are scraped
            if len(products) >= 200:
                break

    return products

try:
    product_data = scrape_noon_products()
    print(f"Scraped {len(product_data)} products successfully.")
finally:
    driver.quit()  


