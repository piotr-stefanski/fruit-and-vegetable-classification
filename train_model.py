import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

# Wczytaj dane z pliku pickle
with open('fruit_data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

data = data_dict['data']
labels = data_dict['labels']

# Mapowanie etykiet na liczby całkowite
label_mapping = {label: idx for idx, label in enumerate(np.unique(labels))}
labels_encoded = np.array([label_mapping[label] for label in labels])

# One-Hot Encoding dla etykiet
labels_encoded_onehot = to_categorical(labels_encoded)

# Podział danych na zbiór treningowy i testowy (w przykładowym kodzie korzystamy z 80% danych do treningu)
X_train, X_test, y_train, y_test = train_test_split(data, labels_encoded_onehot, test_size=0.5, random_state=42)

# Przykładowy model sieci neuronowej
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(len(np.unique(labels)), activation='softmax'))  # Output layer

# Kompilacja modelu
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Trenowanie modelu
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Opcjonalnie: Zapisz wytrenowany model
model.save('fruit_recognition_model.h5')
