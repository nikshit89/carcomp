from flask import Flask, request, jsonify, send_file,render_template, redirect
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd


app = Flask(__name__)
cars_df = pd.read_csv("cars.csv")
model = cars_df['model'].tolist()

@app.route('/')
def my_home():
	return redirect('/car')

@app.route('/car', methods = ['GET', 'POST'])
def compare_care():
	if request.method == 'GET':
		return render_template('myhtml.html')
	elif request.method == 'POST':
		car1 = request.form.get('car1')
		car2 = request.form.get('car2')
		data1 = cars_df[cars_df['model'] == car1]
		data2 = cars_df[cars_df['model'] == car2]
		x1 = list()
		y1 = list()
		x2 = list()
		y2 = list()
		for item in list(data1.columns)[1:]:
			x1.append(item); y1.append(float(data1[item]))
			x2.append(item); y2.append(float(data2[item]))
		plt.plot(x1,y1,color='blue')
		plt.plot(x2,y2,color='red')  
		red_patch = mpatches.Patch(color = 'blue', label=car1)
		blue_patch = mpatches.Patch(color = 'red', label=car2)
		plt.legend(handles = [red_patch, blue_patch])
		plt.savefig('static/file.png', dpi=300)
		plt.close()
		return send_file('static/file.png',mimetype='image/png')



if __name__ == '__main__':
	app.run(host = '127.0.0.1', port = 8000, use_reloader = True, debug = True)
	input()
