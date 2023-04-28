# Load the saved model
from tensorflow.keras.models import load_model

model = load_model('cement_strength_model.h5')

# Make a prediction on a new sample
new_sample = np.array([[200, 100, 50, 150, 10, 1000, 600, 28]])
new_sample_norm = (new_sample - X_train_mean) / X_train_std
prediction = model.predict(new_sample_norm)

# Print the predicted strength
print(f'Predicted cement strength: {prediction[0][0]:.3f}')
