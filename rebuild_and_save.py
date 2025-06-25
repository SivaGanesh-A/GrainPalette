import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras import layers, models

# Load the old model
old_model = load_model("model/rice_model.h5")

# Rebuild the model architecture
IMG_SIZE = (224, 224)
NUM_CLASSES = 5

base = tf.keras.applications.MobileNetV2(input_shape=IMG_SIZE + (3,), include_top=False, weights=None)
model = models.Sequential([
    base,
    layers.GlobalAveragePooling2D(),
    layers.Dense(NUM_CLASSES, activation='softmax')
])

# Set weights from the old model
model.set_weights(old_model.get_weights())

# Save in Keras 3 format (will be compatible with Render)
model.save("model/rice_model.keras", save_format='keras')

print("✅ Rebuilt and saved model in new Keras 3 format.")
