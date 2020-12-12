from flask import Flask, request, jsonify, render_template
import requests

app=Flask(__name__)

api_key='9e90daae1bdc410687b30af57c8976d9';

@app.route('/', methods=['GET','POST'])
def index():
	return render_template("index.html")

@app.route('/search',methods=['GET','POST'])
def search():
	query=request.args.get('query')
	data=requests.get("https://newsapi.org/v2/top-headlines?q="+query+"&apiKey="+api_key).json();
	titles=[]
	urls=[]
	descp=[]
	data=data['articles']
	for i in range(min(len(data),10)):
		temp=data[i];
		titles.append(temp['title'])
		urls.append(temp['url'])
		descp.append(temp["description"])
	return render_template('results.html',titles=titles,urls=urls,descp=descp);

if(__name__ == '__main__'):
	app.run(host='0.0.0.0',port=2512,debug=True)