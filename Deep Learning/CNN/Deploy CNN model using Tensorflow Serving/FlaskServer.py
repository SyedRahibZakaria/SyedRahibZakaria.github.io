from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
import requests
import json

# Initialize the Flask application
app = Flask(__name__)


# route http posts to this method
@app.route('/api/test', methods=['POST'])
def test():
    req_data = request.get_json()

    img = req_data['instances']
    
    data = json.dumps({"signature_name": "serving_default", "instances": img})
    headers = {"content-type": "application/json"}
    json_response = requests.post('http://localhost:9000/v1/models/ImageClassifier:predict', data=data, headers=headers)

    predictions = np.array(json.loads(json_response.text))

    # Decoding results from TensorFlow Serving server
   
    dic = predictions.item()         
    narr = dic['predictions']

    MaxVal = np.amax(narr)
	
    MaxValIndx = np.where(narr == np.amax(narr))
    index = MaxValIndx[1].item()
	
    classList = ["Cat", "Dog", "Person", "False Positive"]
	
    message = "Object detected as " + str(classList[index]) + " with an accuracy of " + str("{0:.2f}".format(MaxVal*100.00)) + "%"

    # return message

    response_pickled = jsonpickle.encode(message)

    return Response(response=response_pickled, status=200, mimetype="application/json")


    # start flask app
if __name__ == "__main__":
	app.run(debug=True)
