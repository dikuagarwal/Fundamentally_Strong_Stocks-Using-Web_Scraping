from flask import Flask, render_template,request
import pandas as pd
import sqlalchemy
import pymysql
import logging
logging.basicConfig(filename="scrapper.log" , level=logging.INFO)


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


# route to html page - "table"
@app.route('/review',methods=["POST"])
def table():

		try:
			if request.method=="POST":
				operation1 = request.form['operation1']
				operator1 = request.form['operator1']
				content1 = request.form['content1']

				operation2 = request.form['operation2']
				operator2 = request.form['operator2']
				content2 = request.form['content2']

				order = request.form['order']
				limit = request.form['limit']
			
		except Exception as e:
			logging.info("Data Fatching error: ",e)
		
		df = pd.read_csv("Screener_Data.csv")

		try:
			engine = sqlalchemy.create_engine("mysql+pymysql://root:@127.0.0.1:3306/fundamental_stocks")
			df.to_sql('stocks', engine, index=False,if_exists="replace")
		except Exception as e:
			logging.info("Sql Engine Problem: ",e)
			exit()

		if limit=='':
			limit = 15		
		
		try:
			if operation2=="None":
				print(operation1)
				query1 = f'''SELECT * FROM fundamental_stocks.stocks where {operation1} {operator1} {content1} order by {order} desc limit {limit} ;'''
				pdf = pd.read_sql(query1,engine)
			else:
				query1 = f'''SELECT * FROM fundamental_stocks.stocks where {operation1} {operator1} {content1} and {operation2} {operator2} {content2} order by {order} desc limit {limit} ;'''
				pdf = pd.read_sql(query1,engine)
		except Exception as e:
			logging.info("Sql query execution error: ",e)
			query1 = '''SELECT * FROM fundamental_stocks.stocks where ROCE>20 and Div_Yld>2.75 order by ROCE desc limit 30 ;'''
			pdf = pd.read_sql(query1,engine)

		return render_template('table.html', tables=[pdf.to_html()], titles=[''])

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int("5000"))
