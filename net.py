from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load your trained model
model = load_model('sinus2.h5')
r"""
# Define image path and model's input dimensions
image_path = 'test.png'
img_height = 128  # Replace with your model's input height
img_width = 128  # Replace with your model's input width

# Load and preprocess the image
image = load_img(image_path, target_size=(img_height, img_width))
image_array = img_to_array(image)
image_array = np.expand_dims(image_array, axis=0)
image_array = image_array / 255.0  # Normalize if necessary

# Make predictions
predictions = model.predict(image_array)
print(predictions)
class_labels = ['A', 'B', 'C']
predicted_class = class_labels[np.argmax(predictions)]

# Output the prediction
print(f"The model predicts the image is of class: {predicted_class}")
"""


def e(matrix):
  for i in range(len(matrix)):
    if matrix[i] == 0:
      matrix[i] = [255, 255, 255]
    else:
      matrix[i] = [0, 0, 0]
  flat_rgb_values = np.array(matrix)

  # Reshape to (128, 128, 3)
  image_shape = (128, 128, 3)
  reshaped_image = flat_rgb_values.reshape(image_shape)
  batch_reshaped_image = np.expand_dims(reshaped_image, axis=0)
  batch_reshaped_image = batch_reshaped_image / 255.0  # Normalize if necessary
  predictions = model.predict(batch_reshaped_image)
  print(predictions)
  return predictions
