# Convolutional Neural Networks in Meteorological Image Classification
### Kristoffer Sorensen -- COMP4449

## About
Using a collection of Very Deep Convolutional Neural Networks along-side a standard CNN for image prediction of meteorological events.

## Data Used
The dataset used was a combination of Kaggle datasets. The first dataset (https://www.kaggle.com/datasets/pratik2901/multiclass-weather-dataset) contained only 4 phenomena to use. Another dataset was used to supplement and provide more selection to train and test the models (https://www.kaggle.com/datasets/jehanbhathena/weather-dataset). Only 7 phenomena were used to start, those being Rain, Hail, Snow, Rain, Cloudy, Sunrise and Shine (Clear). Future plans involve adding more classes to further diversify the dataset.

## Project Goals
The aim for this project is to develop an image classification application capable of using Convolutional Neural Networks to name, classify and detect specific weather phenomena. Using Django as a baseplate to set and deploy 4 unique CNNs on to create an interactive and simple to use application. Future ambitions include developing a way to integrate modeling software into a mobile application or transportation methods for improved safety and alertness.

## Primary Libraries
Since this is a modeling-based project, the main emphasis is on what to use to preform the modeling.
    * Tensorflow (With GPU addition -- NVIDIA GTX 1660 SUPER)
    * Keras (Models came from library)
    * Pandas
    * Pillow
    * Numpy
    * Matplotlib

## EDA
All of the data was clean, with the only issue being resizing the images for model usage (224x224x3). The data was displayed using visuals in order to show count of each class. Data balancing was not an issue as the data was specifically pulled to be as balanced as possible.

## Notes for running on other Operating Systems
This program was developed, tested and completed ALL within WINDOWS and WINDOWS POWERSHELL. When running the code in any other system (Mac, Linux, etc.) be aware that some functions may throw errors due to '/' being in places that others may not have. Some strings to call on other functions (src="/static/imgs/Cloudy_002.jpg") for example require a '/' to start the call in Windows. Please check all STRING CALLS and adjust as appropriate to your specified system.
