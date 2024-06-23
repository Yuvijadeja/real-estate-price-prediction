from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get-locations')
def locations():
    response = jsonify({
        'locations': util.getLocationNames()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get-estimated-price/', methods=['POST'])
def estimator():
    location = request.form['location']
    sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bed = int(request.form['bed'])

    response = jsonify({
        'estimated_price': util.getEstimatedPrice(location, sqft, bath, bed)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    util.loadSavedData()
    print("Starting Python Flask Server for Realt Estate Price Prediction...")
    app.run()