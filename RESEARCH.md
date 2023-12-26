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
