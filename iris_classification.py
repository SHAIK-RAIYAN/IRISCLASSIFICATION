# -*- coding: utf-8 -*-
"""Iris Classification

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ShYjutMhxGWy3yqVmyUBlHVbjOm_KlYh
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
print(iris)
# Create a DataFrame
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# Split the data into features and target
X = iris_df.drop('target', axis=1)
y = iris_df['target']

# Encode target labels
le = LabelEncoder()
y = le.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred_rf = rf_classifier.predict(X_test)

# Evaluate the model
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Random Forest Accuracy: {accuracy_rf}")
print(classification_report(y_test, y_pred_rf))

# Normalize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Build a simple neural network
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(3, activation='softmax')  # Output layer with 3 units for the 3 classes
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_scaled, y_train, epochs=50, batch_size=8, verbose=0)

# Evaluate the model
loss, accuracy_nn = model.evaluate(X_test_scaled, y_test)
print(f"Neural Network Accuracy: {accuracy_nn}")

from sklearn.metrics import f1_score,precision_score,recall_score
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred_rf)

print("f1 score error  :",f1_score(y_test, y_pred_rf,pos_label='positive',average='micro'))
print("Precision Score : ",precision_score(y_test, y_pred_rf,pos_label='positive',average='micro'))
print("Recall Score : ",recall_score(y_test, y_pred_rf , pos_label='positive',average='micro'))

import seaborn as sbn
import matplotlib.pyplot as plt

# Assuming you already have the iris_df DataFrame
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

# Calculate the correlation matrix
correlation_matrix = iris_df.corr()

# Create a heatmap
sbn.heatmap(correlation_matrix, annot=True)

# Show the plot
plt.show()

