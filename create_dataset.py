import os
import pickle
import cv2
import numpy as np

DATA_DIR = 'C:\\Users\\Radziulek\\Desktop\\data_fruit'

data = []
labels = []

# Przygotuj listę dostępnych kategorii (owoce)
categories = os.listdir(DATA_DIR)

for category in categories:
    print(category)
    category_path = os.path.join(DATA_DIR, category)

    for img_path in os.listdir(category_path):
        img = cv2.imread(os.path.join(category_path, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Dostosowanie rozmiaru zdjęć
        img_resized = cv2.resize(img_rgb, (128, 128))

        # Przykład: normalizacja wartości pikseli do zakresu [0, 1]
        img_normalized = img_resized / 255.0

        data.append(img_normalized)
        labels.append(category)  # Dodawanie nazw kategorii bezpośrednio do labels

print(labels)

# Konwersja listy na tablicę numpy
data = np.array(data)
labels = np.array(labels)

# Zapisz dane i etykiety do pliku pickle
with open('fruit_data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
