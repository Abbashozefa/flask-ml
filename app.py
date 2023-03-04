from flask import Flask,render_template,request
import pickle
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    rooms=int(request.form["rooms"])
    distance=int(request.form["distance"])
    prediction=model.predict([[rooms,distance]])
    output=round(prediction[0],3)
    return render_template('index.html',prediction_text=f'A house with {rooms} rooms and located {distance} meters from the city center has a value of ${output}')

@app.route("/hello")
def helloworld():
    return "<h1>Hello Flask App</h1>"




if __name__  == "__main__":
    app.run()