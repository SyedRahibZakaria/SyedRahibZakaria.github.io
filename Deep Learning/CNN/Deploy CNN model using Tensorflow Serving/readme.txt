

Guidelines to run Tensorflow Serving Server:

To run the Tensorflow-Serving Server:

tensorflow_model_server --model_base_path=/home/rahib/Desktop/TensorflowServing/keras-and-tensorflow-serving/my_image_classifier --rest_api_port=9000 --model_name=ImageClassifier

Note:

model_base_path is the absolute path. Change the model_base_path value according to the my_image_classifier directory of your local computer by running the pwd command while in the my_image_classifier directory.




