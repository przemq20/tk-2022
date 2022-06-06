import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.vgg19 import decode_predictions


class ThingsDetector:
    TARGET_SIZE = (224, 224)

    def __init__(self):
        self.model = tf.keras.applications.VGG19(weights='imagenet', include_top=True)

    def _load_img(self, path):
        image = tf.keras.preprocessing.image.load_img(
            path,
            target_size=ThingsDetector.TARGET_SIZE,
        )

        x = tf.keras.preprocessing.image.img_to_array(image)
        x = np.expand_dims(x, axis=0)
        x = tf.keras.applications.vgg19.preprocess_input(x)
        return x

    def detecto(self, image_path, top=5):
        img = self._load_img(image_path)

        predictions = self.model.predict(img)
        decoded_predictions = decode_predictions(predictions, top=top)[0]

        classes = {pred[1] for pred in decoded_predictions}
        return classes

