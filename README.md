# Fundamentally_Strong_Stocks-Using-Web_Scraping
This web scraping project uses Python and MySQL database to gather information about fundamentally strong stocks for investment purpose.
Additionally, we design a user interactive web page and connect it to a python server using Flask API.

This project Divided in two parts:
1. Solving Problem Statment
2. Designing a user interactive web page and connecting it to our python server using flask API.

   
## Problem Statment:

- Screener is one of the most popular website for getting inforamtion about all listed stocks in indian share market.
![image](https://github.com/harshjalan0602/Fundamentally_Strong_Stocks-Using-Web_Scraping/assets/129959008/67114907-1cec-49aa-8716-dc05ea814943)
- Screener has large collection of stocks database that includes various fundamentals details of stocks.
- These Share's fundamental information can be used to choose strong fundamental shares for investing in share market.
- The idea of our project is to scrap the stock data from screener website and create an analysis that can assist investors in making decision regarding which stocks to include in their portfolios, with the aim of maximizing returns.

## Dataset:

- 1250+ records and has 12 columns.

## Solution Details:

- Extracting all the details of share like name, ROCE, Divided yield, Quartely Sales and Profit growth etc. from a javaascript driven webpagewith help of selenium library and store the data in pandas dataframe.
- Established the connection with MySQL Databases with help of sqlalchemy library and store our dataframe in MySQL databases as form of table.
- Execute the sql query on table in order to get desired output.
- Finally store the output shortlisted stocks in "Final_result.csv" file.

## Conclusion:

Based on our analysis, we have shortlisted stocks that meet the following criteria.

  1. The return on Capital Employed (ROCE) is greater than 20%
  2. The dividend yield is equal to or greater than saving account interest rate of 2.75%

These shortlisted stocks have demonstrated strong profitibility and divided potential, making them promising candidates for inclusion in investment portfolios.
