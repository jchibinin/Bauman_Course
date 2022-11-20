import flask
from flask import render_template

import pickle
from sklearn.tree import DecisionTreeRegressor
#1.1.3

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods = ['POST','GET'])

@app.route('/index', methods= ['POST','GET'])

def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
       
        with open('model_d.pkl','rb') as f:
            model_d = pickle.load(f)

        with open('model_w.pkl','rb') as f:
            model_w = pickle.load(f)

        IW	 =  float(flask.request.form['IW'])
        IF	 =  float(flask.request.form['IF'])
        VW	 =  float(flask.request.form['VW'])
        FP   =  float(flask.request.form['FP'])

        depth = model_d.predict([[IW,IF,VW,FP]])
        width = model_w.predict([[IW,IF,VW,FP]])
        print(depth)

        return render_template('main.html', resultd = depth, resultw = width)

if __name__ == '__main__':
    app.run(debug=True)

