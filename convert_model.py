from tensorflow.keras.models import load_model

# Load your existing .h5 model
model = load_model("model/rice_model.h5")

# Save it in new .keras format
model.save("model/rice_model.keras")

print("✅ Model successfully converted to .keras format.")
