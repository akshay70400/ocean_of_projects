from flask import Flask,render_template,request
import os,requests,pickle,jsonify,sklearn
import numpy as np
import database_connect

app=Flask(__name__)

current_path = os.getcwd()
pickle_path = os.path.join(current_path, "assets", "loan_predict.pkl")
model = pickle.load(open(pickle_path, "rb"))

@app.route("/")
@app.route("/home",methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    if request.method=='POST':
        loan_amnt=int(request.form['loan_amnt'])
        term=int(request.form['term'])
        int_rate=float(request.form['int_rate'])
        emp_length=float(request.form['emp_length'])
        home_ownership=int(request.form['home_ownership'])
        annual_inc=float(request.form['annual_inc'])
        annual_inc=np.log(annual_inc)
        purpose=int(request.form['purpose'])
        addr_state=int(request.form['addr_state'])
        dti=float(request.form['dti'])
        delinq_2yrs=float(request.form['delinq_2yrs'])
        revol_util=float(request.form['revol_util'])
        total_acc=float(request.form['total_acc'])
        longest_credit_length=float(request.form['longest_credit_length'])
        verification_status=int(request.form['verification_status'])
        prediction=model.predict([[loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status]])
        output=int(prediction)
        database_connect.insert_record(loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status,output)
        if output==0:
            return render_template('index.html',prediction_text="It does not lead to Defaulter Customer")

        else:
            return render_template('index.html',prediction_text="It leads to Defaulter Customer")
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)