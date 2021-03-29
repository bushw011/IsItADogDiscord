from keras.applications.resnet50 import ResNet50
import numpy as np
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.preprocessing import image                  
from tqdm import tqdm
from os import listdir
from PIL import Image
from io import BytesIO
import requests
class isItDog: 
    def __init__(self):
        # define model
        self.model = ResNet50(weights='imagenet')
    
    def dog_detector(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((224, 224))
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)
        prediction = np.argmax(self.model(img_data))
        return ((prediction <= 268) & (prediction >= 151))

