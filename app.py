from bs4 import BeautifulSoup as bs
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import sqlalchemy
import pymysql

logging.basicConfig(filename="scrapper.log" , level=logging.INFO)

service = Service('path_to_chromedriver')  
chrome_options = Options()
chrome_options.add_argument('--headless')#  # Run Chrome in headless mode, remove this line if you want to see the browser window
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration, as it may cause issues in headless mode
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disable logging of DevTools messages
driver = webdriver.Chrome(service = service,options=chrome_options)


url_pattern = f"https://www.screener.in/screens/29729/top-1000-stocks/?page={1}"
driver.get(url_pattern)
table = driver.find_element(By.CLASS_NAME, "data-table")

# Extract the table headers
headers = ([th.text.strip() for th in table.find_elements(By.TAG_NAME, "th")])[0:12]
# print(headers)

# Empty list to store all the stock data
stock_data = []

# Iterate through all the pages
for page in range(1, 51):
    # Construct the URL for the current page
    url = f"https://www.screener.in/screens/29729/top-1000-stocks/?page={page}"

    # Load the page
    driver.get(url)

    # Find the table containing the stock data
    table = driver.find_element(By.CLASS_NAME, "data-table")
    
    # Extract the table rows
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Extract the data from each row
    for row in rows[1:-1]:
        data = [td.text.strip() for td in row.find_elements(By.TAG_NAME, "td")]
        if len(data)==0:
            pass
        else:
            stock_data.append(data)

# Quit the driver
driver.quit()

df = pd.DataFrame(stock_data, columns=headers)
df.to_csv("All_Stocks_Row_Data.csv",index=False)


# Data Cleaning
ndf = pd.read_csv("All_Stocks_Row_Data.csv",na_values=["not available","n.a."],index_col=[0])

new_df = ndf[["Name","CMP Rs.","P/E","Mar Cap Rs.Cr.","Qtr Profit Var %","Qtr Sales Var %","Div Yld %","ROCE %"]]


new_df.rename(columns={"CMP Rs.":"CMP","P/E":"P2E_Ratio","Div Yld %":"Div_Yld","ROCE %":"ROCE","Mar Cap Rs.Cr.":"Market_Cap","Qtr Profit Var %":"Qtr_Profit_Growth","Qtr Sales Var %":"Qtr_Sales_Growth"},inplace=True)

new_df.to_csv("Screener_Data.csv",index=False)

# engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost:3306/webscraping")

# new_df.to_sql('stocks', engine, index=False,if_exists="replace")

# query = '''SELECT * FROM webscraping.stocks where ROCE>20 and Div_Yld>2.75 order by ROCE desc limit 30 ;'''

# pdf = pd.read_sql(query,engine)

# print(pdf)
