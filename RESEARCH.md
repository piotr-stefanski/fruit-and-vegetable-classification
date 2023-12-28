# [Template]
# Research
## Title
URL:
Authors:
### Abstract and results
### Methodology
---
# Analysis of Artificial Intelligence based Image Classification Techniques
### URL: [link](https://www.researchgate.net/profile/Subarna-Shakya/publication/341064540_Analysis_of_Artificial_Intelligence_based_Image_Classification_Techniques/links/6106237d169a1a0103cc9c47/Analysis-of-Artificial-Intelligence-based-Image-Classification-Techniques.pdf?origin=journalDetail&_tp=eyJwYWdlIjoiam91cm5hbERldGFpbCJ9)
##### **Authors**: Dr. Subarna Shakya Professor, Department of Electronics and Computer Engineering, Central Campus, Institute of Engineering, Pulchowk, Tribhuvan University.

### Abstract and results:
The work discusses accuracy of different classifiers, such as Support Vector Machine (SVM), K-Nearest Neighbor (KNN), Random Forest (RF), and Discriminant Analysis (DA). As a result, it proposes utilizing a KNN classifier for very efficient fruit image classification, achieving an accuracy of 93.103%, and recommends integrating the methodology with a weighing machine to expedite billing by capturing a sample fruit image for algorithmic classification, while highlighting the importance of improving specificity and negative predictive value (NPV) to address real-time challenges, suggesting enhanced performance for evaluating mixed fruits through increased training with such images. 
### Methodology
**Data set** (`Training Img data`, `Testing Img data`) -> **Preprocessing** (`Resizin`, `gray scale`, `edge protection`) -> **Feature extraction** (`Color`, `Binarization`, `Border`, `Texture`, `Threshold`) -> **Classifier** -> **Result**

---

# High performance vegetable classification from images based on AlexNet deep learning model
### URL: [link](https://www.ijabe.org/index.php/ijabe/article/view/2690/pdf)
##### **Authors**: Ling Zhu, Zhenbo Li, Chen Li, Jing Wu, Jun Yue

### Abstract and results:
This work introduces a high-performance deep learning method for automatically classifying vegetable images. The study employs the AlexNet network model in Caffe, utilizing ImageNet data for training and testing. The use of Rectified Linear Units (ReLU) in the output function accelerates network training, and dropout technology enhances model generalization. Experimental results demonstrate that, with varying amounts of training data, the deep learning method achieves a 92.1% accuracy rate on the test set. 
### Methodology
**Dataset** (`ImageNet`,`24000 images after data expansion`, `80% train`, `20% test`, `5 classes`) -> **Preprocessing** (`rotation`, `resize - 80x80`) -> **Classifier** (`Caffe Framework`, `AlexNet CNN`, `Rectified Linear Units (ReLU)`) -> **Result**

---

# Research
## Automatic fruit and vegetable classification from images
URL: [link](https://www.sciencedirect.com/science/article/pii/S016816990900180X?casa_token=1wcxDcLxWpwAAAAA:whpruQsTS73A7mAN2TMgqtKuhi_PdzjQFQXaViDxq7rIge__tMs20TmO1GDSy5AqP2fAqHHArg#sec16)
##### **Authors**: Anderson Rocha, Daniel C. Hauagge, Jacques Wainer, Siome Goldenstein
### Abstract and results:
This paper introduces a unified approach that can combine many features and classifiers that requires less training and is more adequate to some problems than a naive method, where all features are simply concatenated and fed independently to each classification algorithm. The results show that the introduced solution is able to reduce the classification error in up to 15 percentage points with respect to the baseline.
### Methodology
**Dataset** (`Supermarket Produce`, `15 classes`) ->  **Image Descriptors** (`Global Color Histogram (GCH)`, `Unser’s descriptors`, `Color coherence vectors (CCVs)`, `Border/interior (BIC)`, `Appearance descriptors`) -> **Supervised learning techniques** (`Linear Discriminant Analysis (LDA)`, `Support Vector Machines (SVMs)`, `Classification Trees`, `Neural Networks (NNs)`) -> **Background substracion** (`Otsu`, `Meanshift`, `Normalized cuts`, `K means algorithm`)

---

## Hyperspectral fruit and vegetable classification using convolutional neural networks
### URL: [link](https://www.sciencedirect.com/science/article/pii/S0168169918315680?casa_token=kVxl8ygp2vAAAAAA:qUzsHkNT_7_7AdtZ9hkVIoPgL71RpJ9mpWMqc_TIF7DK4m0Ay3WupFkYWRhdEjH6b6R219he)
##### **Authors**: Jan Steinbrener, Konstantin Posch, Raimund Leitner
### Abstract and results:
The study employs pre-trained convolutional neural networks (CNNs) designed for RGB images to classify challenging fruits and vegetables with similar appearances using hyperspectral images. By fine-tuning the networks with a custom hyperspectral dataset and including a data compression layer, they achieved a notable increase in average classification accuracy from 88.15% to 92.23% (Kernel-model). This adaptable approach holds promise for broader applications beyond fruit and vegetable classification.
### Methodology
**Dataset** (`Custom Dataset`, `2700 images of 13 different classes`, `700 - Validation`, `2000 - Train`) -> **Preprocessing** (`resize - 256 x 256`, `rescalling`) -> **Classifier** (`Pseudo-RGB model`,`Linear combination model`,`Kernel-model`) -> **Results**

---

## Fruit Classification for Retail Stores Using Deep Learning
### URL: [link](https://link.springer.com/chapter/10.1007/978-3-030-49076-8_1)
##### **Authors**: Jose Luis Rojas-Aranda, Jose Ignacio Nunez-Varela, J. C. Cuevas-Tello & Gabriela Rangel-Ramirez 
### Abstract and results:
The study presents a method for fruit classification using Convolutional Neural Networks (CNN) to expedite the checkout process in stores. The method uses a unique dataset of images and incorporates color-related input features into the CNN architecture. The MobileNetV2 architecture was chosen for its lightweight nature, and the model was trained using transfer learning. The model using the single RGB color obtained the highest accuracy at 0.95 for unbagged and 0.93 for bagged fruits.
### Methodology:
**Dataset** (`Custom Dataset`, `1067 images (725 train, 342 test)`, `3 fruit classes`, `bagged, unbagged`) -> **CNN Architecture** (`MobileNetV2`) -> **Transfer Learning** (`Weights from a model trained with the ImageNet dataset`) -> **Improving MobileNetV2** (`Single RGB Fruit Color``, RGB Histogram``, RGB Centroid Using K-Means`)

---

## Fruit and Vegetable Identification Using Machine Learning for Retail Applications
### URL:[link](https://arxiv.org/pdf/1810.09811.pdf)
##### **Authors**: Frida Femling, Adam Olsson, Fernando Alonso-Fernandez
### Abstract and results: 
This is an industrial method for identifying fruits and vegetables in retail stores, utilizing cameras to capture images. The system assists customers in labeling selected fruits and vegetables with price tags based on their weight. Its goal is to reduce human-computer interactions, expedite the identification process, and enhance the user-friendliness of the graphical interface compared to current manual systems. The hardware comprises a Raspberry Pi, camera, display, load cell, and casing. Various convolutional neural networks were tested and retrained to classify objects. A heuristic evaluation involving multiple users concluded that the implemented system is more user-friendly than existing solutions.
### Methodology:
**Dataset** (`ImageNet`, `400 images per class (in addition 30 images per class have also been collected with the camera)`, `10 classes`) -> **Hardware** (`Raspberry Pi 64bit Quad Core 1.2GHz CPU and has 1GB of RAM, The camera has 8-megapixels`) -> **Convolutional Neural Networks** (`Inception v3`)


