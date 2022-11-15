from django.shortcuts import render
from django.http import HttpResponse
import os
import tensorflow as tf
import numpy as np

# Create your views here.
def page1(request):
    return render(request, 'index.html')

# Add a third page to the second application
def page3(request):
    return render(request, 'index.html')

# Add a fourth page to the second application -- Results page
def page4(request):
    return render(request, 'index.html')

# Add a fifth page to the second application -- Results page
def page5(request):
    return render(request, 'index.html')

#----------------------------------------------------------------

DEFAULT_LIST= '''{
"columns": [0, 1, 2, 3],
"values" : [
    ["id1", "Matrix Multip", "", "https://www.youtube.com/embed/LXKku-IbSak"],
    ["id2", "Life goes on ", "", "https://www.youtube.com/embed/Hg7BGS7ap3I"],
    ["id3", "Mistake/Mystique", "", "https://www.youtube.com/embed/VQrhl7KJ0m4"]
]
}'''

def getmenu(request, topic=None, **kwargs):
    print(f"Getting menu for topic: {topic}") 
    return HttpResponse( DEFAULT_LIST )

#----------------------------------------------------------------

# ResNet50 Model
def runexp(request):
    filename = "NO FILENAME!!!!"
    for f in request.FILES.getlist('file'):
        content = f.read()
        filename = "tmp/" + str(f)
        print(f"++ Save file {filename} Content: {len(content)} :")
        with open(filename, "wb") as f:
            f.write(content)

    # Import the data from the main file(s)
    folders = ["Cloudy", "Hail", "Lightning", "Rain", "Clear", "Snow", "Sunrise"]

    # Bring in the ResNet50 model
    model = tf.keras.models.load_model("models/ResNet50_WX.h5")

    # ResNet50 SAVED Model testing
    img = tf.keras.utils.load_img(
        filename, target_size=(224, 224)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
            
    return HttpResponse( f"This image most likely belongs to {folders[np.argmax(score)]} with a \
        {round(100 * np.max(score), 2)}% confidence.")


#----------------------------------------------------------------

# ResNet152 Model
def runexp_1(request):
    filename = "NO FILENAME!!!!"
    for f in request.FILES.getlist('file_1'):
        content = f.read()
        filename = "tmp/" + str(f)
        print(f"++ Save file {filename} Content: {len(content)} :")
        with open(filename, "wb") as f:
            f.write(content)

    # Import the data from the main file(s)
    folders = ["Cloudy", "Hail", "Lightning", "Rain", "Clear", "Snow", "Sunrise"]

    # Bring in the ResNet50 model
    model = tf.keras.models.load_model("models/ResNet152_WX.h5")

    # ResNet50 SAVED Model testing
    img = tf.keras.utils.load_img(
        filename, target_size=(224, 224)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
            
    return HttpResponse( f"This image most likely belongs to {folders[np.argmax(score)]} with a \
        {round(100 * np.max(score), 2)}% confidence.")

#----------------------------------------------------------------

# 5-Layer standard CNN
def runexp_2(request):
    filename =  "NO FILENAME!!!!"
    for f in request.FILES.getlist('file'):
        content = f.read()
        filename = "tmp/" + str(f)
        print(f"++ Save file {filename} Content: {len(content)} :")
        with open(filename, "wb") as f:
            f.write(content)

    # Import the data from the main file(s)
    folders = ["Cloudy", "Hail", "Lightning", "Rain", "Clear", "Snow", "Sunrise"]

    # Bring in the ResNet50 model
    model = tf.keras.models.load_model("models/BaseCNN_WX.h5")

    # ResNet50 SAVED Model testing
    img = tf.keras.utils.load_img(
        filename, target_size=(224, 224)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
            
    return HttpResponse( f"This image most likely belongs to {folders[np.argmax(score)]} with a \
        {round(100 * np.max(score), 2)}% confidence.")

#----------------------------------------------------------------

# VGG-16 Model
def runexp_3(request):
    filename =  "NO FILENAME!!!!"
    for f in request.FILES.getlist('file_1'):
        content = f.read()
        filename = "tmp/" + str(f)
        print(f"++ Save file {filename} Content: {len(content)} :")
        with open(filename, "wb") as f:
            f.write(content)

    # Import the data from the main file(s)
    folders = ["Cloudy", "Hail", "Lightning", "Rain", "Clear", "Snow", "Sunrise"]

    # Bring in the ResNet50 model
    model = tf.keras.models.load_model("models/VGG16_WX.h5")

    # ResNet50 SAVED Model testing
    img = tf.keras.utils.load_img(
        filename, target_size=(224, 224)
    )

    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
            
    return HttpResponse( f"This image most likely belongs to {folders[np.argmax(score)]} with a \
        {round(100 * np.max(score), 2)}% confidence.")
