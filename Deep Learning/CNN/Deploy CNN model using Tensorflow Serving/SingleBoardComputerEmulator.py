import json
#import tensorflow as tf
import numpy as np
import requests
from keras.preprocessing import image


image_path = "./test_images/A.jpg"
#image = tf.keras.preprocessing.image.load_img(image_path)
img = image.img_to_array(image.load_img(image_path, target_size=(224, 224, 3))) / 255.
img = np.expand_dims(img, axis = 0)
#mod = img.tolist()

# "signature_name": "serving_default", 

data = json.dumps({"instances": img.tolist()})
headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:5000/api/test', data=data, headers=headers)
print (json.loads(json_response.text))
