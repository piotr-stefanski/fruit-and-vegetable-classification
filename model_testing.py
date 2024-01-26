import pickle
import numpy as np
from keras.models import load_model
import cv2

# Wczytaj dane z pliku pickle
with open('fruit_data.pickle', 'rb') as f:
    data_dict = pickle.load(f)

data = data_dict['data']
labels = data_dict['labels']

# Mapowanie etykiet na liczby całkowite
label_mapping = {label: idx for idx, label in enumerate(np.unique(labels))}
labels_encoded = np.array([label_mapping[label] for label in labels])

# Wczytaj wytrenowany model
model = load_model('fruit_recognition_model.h5')
for _ in range(10):
    # Losowo wybierz zdjęcie z danych testowych
    random_index = np.random.randint(0, len(data))
    random_image = data[random_index]
    true_label = labels[random_index]

    # Wyświetl wybrane zdjęcie
    cv2.imshow('Random Image', cv2.cvtColor((random_image * 255).astype(np.uint8), cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Przygotuj dane do predykcji
    input_data = np.expand_dims(random_image, axis=0)

    # Dokonaj predykcji
    predictions = model.predict(input_data)
    predicted_label_idx = np.argmax(predictions)
    predicted_label = list(label_mapping.keys())[list(label_mapping.values()).index(predicted_label_idx)]

    print(f'True Label: {true_label}')
    print(f'Predicted Label: {predicted_label}')
