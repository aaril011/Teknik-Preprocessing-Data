import numpy as np
from sklearn import preprocessing

#Input Data
input_data = np.array([[2.1, -1.9, 5.5],[-1.5, 2.4, 3.5], [0.5, -7.9, 5.6], [5.9, 2.3, -5.8]])
print(input_data)

#Binarization
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)

#Mean Removal
print("Mean =", input_data.mean(axis=0))
print("Std deviation =", input_data.std(axis=0))

data_scaled = preprocessing.scale(input_data)
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", input_data.std(axis=0))

#Min Max Scaling
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin Max scaled data:\n", data_scaled_minmax)

#L1 Normalization
#Normalize data
data_normalized_l1 = preprocessing.normalize(input_data,norm='l1')
print("\nl1 normalized data:\n", data_normalized_l1)

#L2 Normalization
#Normalize data
data_normalized_l2 = preprocessing.normalize(input_data,norm='l2')
print("\nl1 normalized data:\n", data_normalized_l2)
