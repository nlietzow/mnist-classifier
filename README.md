# README


## About The Project

The aim of this project was to practice working with docker and especially containerizing python applications.

To do so, I have trained an image classifier for handwritten digits on the [MNIST dataset](http://yann.lecun.com/exdb/mnist/) using keras. To interact with the model, there is a dashboard which was build using dash for python. After uploading an image via drag and drop, the image is displayed and run through the model. The prediction is then returned below. Using the Dockerfile, an image of the application can be created. This image can also be found in my [https://hub.docker.com/]()

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

This section lists the major frameworks that were used for building the python application.
* [docker](https://getbootstrap.com)
* [tensorflow](https://jquery.com)
* [dash](https://laravel.com)



## Getting Started

There are two ways to run the app. As this project was dedicated to pratice working with docker, primarily it should be run via the docker image. However, there is also the option to run the app directly using the python script.

There are a few image samples for the classifier in mnist_samples.zip for testing the application.

### Running the app in a docker container

1. Clone the repo
   ```sh
   docker clone https://github.com/your_username_/Project-Name.git
   ```
2. Start the application in a container
   ```sh
   docker run -d 8000:8000 mnistdockerdashboard
   ```


### Alternative: Directly running the python script

1. Clone the repo
   ```sh
   git clone https://github.com/nlietzow/mnist-classifier.git
   ```
2. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
3. Run the python script
   ```sh
   python ./app/app.py
   ```


## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.


## Acknowledgements
* [Docker Tutorial For Beginners - How To Containerize Python Applications](https://www.youtube.com/watch?v=bi0cKgmRuiA)
* [The MNIST database of handwritten digits](http://yann.lecun.com/exdb/mnist/)
* [Training a neural network on MNIST with Keras](https://github.com/tensorflow/datasets/blob/master/docs/keras_example.ipynb)

