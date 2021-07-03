## About The Project

The aim of this project was to practice working with Docker and, in particular, containerizing Python applications.

To do so, I trained an image classifier for handwritten digits on the [MNIST dataset](http://yann.lecun.com/exdb/mnist/) using Keras. To interact with the model, there is a dashboard build with dash for python.After uploading an image, it is displayed and run through the model.  The prediction is then returned below. The Dockerfile is used to create a Docker image of the application. This image can also be found in my [Docker Hub](https://hub.docker.com/repository/docker/niclaslietzow/mnist-classifier).

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

This section lists the major frameworks that were used for building the python application.
* [Docker](https://www.docker.com/)
* [TensorFlow](https://www.tensorflow.org/)
* [Dash apps](https://plotly.com/dash/)



## Getting Started

There are two ways to run the app. Since this project was dedicated to practicing working with Docker, it should primarily be run via the Docker image. However, there is also the option to run the app directly via the Python script.

In the file mnist_samples.zip there are some image samples for the classifier to test the application.

### Running the app in a docker container

1. Make a copy of the docker image
   ```sh
   docker pull niclaslietzow/mnist-classifier
   ```
2. Run the application in a container
   ```sh
   docker run -p 8000:8000 mnist-classifier
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


## Acknowledgements
* [Docker Tutorial For Beginners - How To Containerize Python Applications](https://www.youtube.com/watch?v=bi0cKgmRuiA)
* [The MNIST database of handwritten digits](http://yann.lecun.com/exdb/mnist/)
* [Training a neural network on MNIST with Keras](https://github.com/tensorflow/datasets/blob/master/docs/keras_example.ipynb)
