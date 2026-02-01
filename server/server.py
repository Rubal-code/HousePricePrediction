from flask import Flask ,request,jsonify
from flask_cors import CORS
import util
# import database

app=Flask(__name__)
CORS(app)
# database.init_db()

@app.route("/")
def home():
    return "Real Estate Price Prediction API Running"

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({

        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    estimated_price=util.get_estimated_price(location, total_sqft, bhk, bath)

    # try:
    #     database.log_prediction(location,total_sqft,bhk,bath,estimated_price)
    #     print(f"Logged prediction: {location}, {total_sqft} sqft, Price: {estimated_price} Lakhs")
    # except Exception as e:
    #     print(f"--database logging failed--error :{e}")    

    response = jsonify({
        'estimated_price':estimated_price
    })
    return response

if __name__=="__main__":
    util.load_saved_artifacts()
    print("starting python flask server for homeprice prediction...")
    app.run(debug=True)    


# cd "D:\REAL ESTATE\BHP\server"
# python server.py
