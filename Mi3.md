## Methodology
In this study we have used a variety of machine learning models for the detection of diseases including heart disease, diabetes and detection of pneumonia. The main approach that we are adopting to train our model includes firstly, data pre-processing (normalization, missing value imputation, converting images to grayscale and resizing image to a standard size.). Secondly, we will be diving our dataset into train, test and validation in order to train and test our model. Lastly, we will optimize our model by changing hyper parameters.

## Dataset
The first and foremost step in the process of developing a machine learning model includes the collection of clinical datasets and records which forms the foundation for training the model and  maximizing its accuracy over validation datasets. Tabular or structured data are the most common type of datasets that are used in machine learning models and are mostly in the form of csv files. This is what we have used for training and validating our models as well. This case study includes three models for the purpose of heart disease, diabetes and pneumonia detection. Below we have briefly discussed the datasets used for training and validating each of these models.

## Dataset for Heart Disease Detection Model 
For the training of heart disease detection model, we have used the dataset that has been  provided by the University of California Irvine available in the UCI repository of Kaggle. This dataset has been extensively used and exploited for research purposes all around the world. Andras Janosi (Hungarian Institute of Cardiology. Budapest), William Steinbrunn (University Hospital, Zurich, Switzerland ), Matthias Pfisterer (University Hospital, Basel, Switzerland) and Robert Detrano (V.A. Medical Center, Long Beach and Cleveland Clinic Foundation) are the contributors of this dataset. This dataset consists of 13 attributes along with 1 outcome column. Talking about instances this dataset consists of 303 instances with 13 unique attributes for each one and a target column. 

## Dataset for Diabetes Detection Model
The dataset used for the training and validation purpose of the diabetes detection model has been curated from  the University of California Irvine repository available on Kaggle. This dataset has been originally grasped from the National Institute of Diabetes and Digestive and Kidney Diseases. This dataset was built with the objective to assist the machine learning model in the prediction of whether a person has diabetes or not, on the basis of analytical and clinical measurements that are already included in the dataset. The given dataset consists of 8 attributes and a target column with binary value (either 0 or 1) indicating the presence or absence of diabetes for each instance. The attributes included were Age, Diabetes Pedigree Function, Body Mass Index, Insulin, skin thickness, blood pressure, glucose level, and number of pregnancies.  Counting them all, this dataset embraces around 768 instances.


## Dataset for Pneumonia Detection Model
The dataset which we are using to train our model to detect the presence of pneumonia is taken from the repository of the University of California San Diego available on data.mendeley . In this project we have used various models such as Logistic Regression, Random Forest Classifier, Support Vector Machine and Convolutional Neural Network.  The creators and contributors of this data set are Daniel Kermany, Kang Zhang, Michael Goldbaum. This dataset has been divided into three main sections: training, testing and validating along with subfolders for each image type, which either pneumonia or normal. The anterior and posterior X-rays of the chest were chosen from previous groups patients aged one to five years at Guangzhou Women and Children's Medical Center in Guangzhou. All the chest X-rays were conducted as a part of patient’s regular clinical routine. The analysis of the chest x-ray was done by following a thorugh process. The radiograph s for all the chest x-rays were firstly filtered
by removing out all the scans with low quality or illegible reports. These diagnostic images were then evaluated by some expert physicians
before sending it out for training the AI model. In order to cross check and validate any errors that may have occured during the evaluation 
process done by the experts, the images were checked again by a panel of experts.


## Models
In this section we have primarily covered the various types of Machine Learning models which have been incorporated in the detection of the disease. Some of the models which have been implemented are: Logistic Regression, support vector machine (SVM), convolutional neural networks (CNN) and random forest classifier. Below we have briefly elaborate upon each of these models and their application in this study.
Logistic Regression
Logistic regression model is a fairly common one which is used for classification task in the fields of statistics and machine learning. Logistic regression model uses the probability of a sample belonging to a particular class. This model can be used for binomial as well as multinomial classification. The logistic regression model uses sigmoid function on the linear regression hypothesis function. This sigmoid function is given by the following equation:
The sigmoid function ensures that the value is between 0 and 1. We have used this model for heart disease prediction. We have also applied some hyper parameter optimizations, thus improving the accuracy of our model.

## CNN
CNNs are one of the most popular models in the field of deep learning. These are mostly used in tasks related to images/pictures.  A basic CNN consists of an input layer, convolutional layer, a pooling layer and a dense layer. The activation functions commonly used in CNN are : relu and sigmoid. The full form of relu is Rectified Linear Unit. Mathematically, it is defined as y = max(0, x).  
Sigmoid function is usually placed at the last layer in the CNN model. It converts the output of the model into a probability, ie, it scaled the output of the model in the range of 0 and 1.
We have used the CNN model for pneumonia detection. Since we are using chest x-ray images for our classification, CNN seems to be the best model as it can handle image data effectively. We have created a multi-layer deep CNN model which consists of multiple 2-D convolutional layers. It also consists of 2-D max pooling layers, a dense layer and a final output layer. We have also used SGD optimizer during the compilation of the model.

## Random Forest Classifier
Random Forest Classifier Algorithm is one of the most popular machine learning algorithms that is used in the study of supervised learning. This Classifier algorithm can be used for both classification and regression machine learning problems. Random Forest Classifier is formulated upon the technique of ensemble learning. In the process of ensemble learning we integrate the results of multiple decision tree classifiers and provide a solution for a more complex and critical problem.  The nodes of decision tree are selected on the basis of Gini impurity or information gain.
Equation: https://victorzhou.com/blog/gini-impurity/
The Random Forest Algorithm extracts the prediction results of all the decision trees and average them out to get the final output with much improved accuracy. In this study random forest algorithm has been used for diabetes and heart disease prediction

## SVM
Support Vector Machine (SVM) is a supervised learning method used in machine learning. SVM can be used for classification and regression task. In case of classification tasks the goal of Support Vector Machine is to find a decision boundary. The Equation of decision boundary is given as. 
w⋅x+b=0 
SVM has many kernel functions which can be used for non-linear classification. Some of the popular kernel functions are Linear, RBF, Polynomial, Sigmoid. We have used SVM in heart disease and diabetes detection models.



