import base64
import numpy as np
from PIL import Image
import tensorflow as tf
import os


def image_processing(content, temp_path):
    """ "
    Takes in an uploaded image and saves it temporarly in the working directory.
    The image is then processed to an numpy array and scaled for the tensorflow model.

    Parameters:
        content:
        temp_path:

    Returns:
        final_image:
    """

    data = content.encode("utf8").split(b";base64,")[1]
    with open(temp_path, "wb") as fp:
        fp.write(base64.decodebytes(data))

    image_orig = Image.open(os.path.abspath("app/temp/image.jpg"))
    image_rgb = Image.new("RGB", image_orig.size)
    image_rgb.paste(image_orig)
    test_image = image_rgb.resize((28, 28))

    np_image = np.array(test_image)[:, :, 0]
    np_image = tf.cast(np_image, tf.float32) / 255.0

    final_image = np.expand_dims(np_image, 0)

    return final_image
