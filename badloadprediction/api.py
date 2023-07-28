from flask import Flask,render_template,request,jsonify
import requests,os,pickle,sklearn
import numpy as np

app=Flask(__name__)


current_path = os.getcwd()
pickle_path = os.path.join(current_path, "assets", "loan_predict.pkl")
model = pickle.load(open(pickle_path, "rb"))

@app.route("/")
@app.route("/home",methods=['GET'])
def home():
    return render_template("index.html")




@app.route("/api/predict",methods=["POST"])
def predict_api():
    data = request.get_json()
    if request.method=='POST':
        loan_amnt=int(data['loan_amnt'])
        term=int(data['term'])
        int_rate=float(data['int_rate'])
        emp_length=float(data['emp_length'])
        home_ownership=int(data['home_ownership'])
        annual_inc=float(data['annual_inc'])
        annual_inc=np.log(annual_inc)
        purpose=int(data['purpose'])
        addr_state=int(data['addr_state'])
        dti=float(data['dti'])
        delinq_2yrs=float(data['delinq_2yrs'])
        revol_util=float(data['revol_util'])
        total_acc=float(data['total_acc'])
        longest_credit_length=float(data['longest_credit_length'])
        verification_status=int(data['verification_status'])
        prediction=model.predict([[loan_amnt,term,int_rate,emp_length,home_ownership,annual_inc,purpose,addr_state,dti,delinq_2yrs,revol_util,total_acc,longest_credit_length,verification_status]])
        output=prediction[0]
        if output==0:
            return jsonify("It is not a loan Defaulter")
        return jsonify("It is loan Defaulter")


if __name__=="__main__":
    app.run(debug=True)