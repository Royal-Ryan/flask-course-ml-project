from flask import Flask, url_for, render_template
from forms import InputForm
import pickle
import numpy as np


app= Flask(__name__)
app.config["SECRET_KEY"]=  "secret_key"


label_encoder=pickle.load(open('label_encoder.pickle','rb'))
model=pickle.load(open('crop_recommendation_model.pickle','rb'))
mms=pickle.load(open('min_max_scaler.pickle','rb'))

def suggest(N,P,K,temperature, humidity, ph, rainfall):
        data=(N,P,K,temperature, humidity, ph, rainfall)
        data=np.array(data).reshape(1,-1)
        data=mms.transform(data)
        y_pred=model.predict(data)
        return label_encoder.inverse_transform(y_pred)[0]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home Page")

@app.route("/recommend",methods=["GET","POST"])
def recommend():
    form=InputForm()
    if form.validate_on_submit():
        N=  form.N.data
        P=  form.P.data
        K=  form.K.data
        temperature=    form.temperature.data
        humidity=   form.humidity.data
        pH= form.ph.data
        rainfall=   form.rainfall.data
        result = suggest(N, P, K, temperature, humidity, pH, rainfall)
        message= f"The recommended crop is: {result}"
    else:
         message="Please provide the valid input details!"
    return render_template("recommend.html",title="Recommend",form=form,output=message)


if __name__=="__main__":
    app.run(debug=True)