
from ast import keyword
from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
from flask_pymongo import PyMongo
import arxiv
import json



# df=pd.read_csv('arxiv.csv', index_col=0)
app = Flask(__name__)

@app.route("/",methods=("POST", "GET"))
def index():

    if request.method == 'GET':

    # df = data.data_table()
    
    # return arxiv_data
    # df=data.data_table()
    # return render_template("index.html", tables=[arxiv.data_frame()])
        df=arxiv.data_frame()
        return render_template('index.html',  tables=[df.to_html(classes='table', header="true")])
        
    elif request.method == 'POST':
        results = request.form
        # list_of_input= results.to_list()

        # keyword_input = json.dumps(results)
        # with open('data.json', 'w', ) as f:
        #     json.dump(results, f,)
        inquiries=results['text'].split(',')
        arxiv.arxiv_reload(inquiries)
        return redirect('/', code=302) 
        # return "post request"

# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/api_app"
# mongo = PyMongo(app)


# @app.route("/")
# def index():
    
#     api_app=mongo.db.api_app.find_one()
#     return render_template('index.html',  api_app=api_app)
#     # return render_template('index.html', api_app=api_app)

    


# @app.route("/data/")
# def data():
#    api_app = mongo.db.api_app
#    print(api_app)
#    api_data = data.data_table()
#    api_app.update({}, api_data, upsert=True)
#    return redirect('/', code=302)


if __name__ == "__main__":
   app.run(debug=True)