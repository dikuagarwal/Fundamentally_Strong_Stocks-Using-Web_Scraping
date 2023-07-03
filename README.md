# Fundamentally_Strong_Stocks-Using-Web_Scraping
This web scraping project uses Python and MySQL database to gather information about fundamentally strong stocks for investment purpose.
Additionally, we design a user interactive web page and connect it to a python server using Flask API.

This project Divided in two parts:
1. Designing a user interactive web page and connecting it to our python server using flask API.
2. Solving Problem Statment

### Key-Skills:
- Python - Pandas - MySQL - Flask - HTML - CSS
- Data Analysis - Stock Market Fundamentals - Web Scraping
   
## Problem Statment:

- Screener is one of the most popular website for getting inforamtion about all listed stocks in indian share market.
![image](https://github.com/harshjalan0602/Fundamentally_Strong_Stocks-Using-Web_Scraping/assets/129959008/67114907-1cec-49aa-8716-dc05ea814943)
- Screener has large collection of stocks database that includes various fundamentals details of stocks.
- These Share's fundamental information can be used to choose strong fundamental shares for investing in share market.
- The idea of our project is to scrap the stock data from screener website and create an analysis that can assist investors in making decision regarding which stocks to include in their portfolios, with the aim of maximizing returns.

## Dataset:

- 1250+ records and has 12 columns.

## User Interactive Web-page:

- Users will interact with our Python server through this web page.
- Users can apply their own choice filters (such as a P/E ratio greater than 15, dividend yield greater than 5%, etc.) on the stock database to retrieve fundamentally strong stocks data.
- Additionally, users have the option to set the top N number of shares that they want to display. The default value for N is 15.
![image](https://github.com/harshjalan0602/Fundamentally_Strong_Stocks-Using-Web_Scraping/assets/129959008/bd1625bb-cceb-49c6-8378-00efb1cd2a8f)
- After filling the form and click on submit button, the web page send a request to the python server using HTML forms, specifying the HTTP method as "POST".
- The Flask server receives the request and maps it to a specific route defined in the Flask application. The Flask route handler function processes the request data.
- The Flask server prepares a response, and sends back to the client, that containing the desired stock data based on the applied filters and additional processing.
- The web page receives the response from the Flask server and updates its display to present the retrieved stock data to the user.
![image](https://github.com/harshjalan0602/Fundamentally_Strong_Stocks-Using-Web_Scraping/assets/129959008/d9d93ab0-fb61-4962-bc34-90d917c9a88c)

## Solution Details:

- Extracting all the details of share like name, ROCE, Divided yield, Quartely Sales and Profit growth etc. from a javaascript driven webpagewith help of selenium library and store the data in pandas dataframe.
- Established the connection with MySQL Databases with help of sqlalchemy library and store our dataframe in MySQL databases as form of table.
- Execute the sql query on table in order to get desired output.
- Finally store the output shortlisted stocks in "Final_result.csv" file.

# Conclusion:

Based on our analysis, we have shortlisted stocks that meet the following criteria.

  1. The return on Capital Employed (ROCE) is greater than 20%
  2. The dividend yield is equal to or greater than saving account interest rate of 2.75%

![image](https://github.com/harshjalan0602/Fundamentally_Strong_Stocks-Using-Web_Scraping/assets/129959008/3cd5830e-6b46-415a-a670-a93873f60fbe)

These shortlisted stocks have demonstrated strong profitibility and divided potential, making them promising candidates for inclusion in investment portfolios.
