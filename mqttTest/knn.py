import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from server import send_data
import pickle
import csv

data2 = []

with open('iris.data', 'r') as file:
	csv_reader = csv.reader(file, delimiter =",")
	for row in csv_reader: 
            try:
                data2.append([float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]])
            except: 
                pass
data2 = np.array(data2)
print(data2[:,1:4])
train, test = train_test_split(data2, test_size = 0.2, stratify = data2[:,4], random_state = 42)
print(train)
X_train = train[:,0:4]
y_train = train[:,4]
X_test = test[:,0:4]
y_test = test[:,4]

dict = {"a":X_train,"b":y_train}
send_data(dict)
mod_10nn1=KNeighborsClassifier(n_neighbors=10) 
mod_10nn1.fit(X_train[:20],y_train[:20])
prediction=mod_10nn1.predict(X_test[:5])
print('The accuracy of the 5NN Classifier is',"{:.3f}".format(metrics.accuracy_score(prediction,y_test[:5])))
print(prediction)

mod_10nn2=KNeighborsClassifier(n_neighbors=10) 
mod_10nn2.fit(X_train[20:],y_train[20:])
prediction=mod_10nn2.predict(X_test[5:10])
print('The accuracy of the 5NN Classifier is',"{:.3f}".format(metrics.accuracy_score(prediction,y_test[5:10])))
print(prediction)


attr = mod_10nn1.__dict__


for k, v in attr.items():
    if isinstance(v, list) and v[-1:] == '_':
        attr[k] = v.tolist()


with open('filename.pickle', 'wb') as handle:
    pickle.dump(attr, handle, protocol=pickle.HIGHEST_PROTOCOL)
b=""
with open('filename.pickle', 'rb') as handle:
    b = pickle.load(handle)
    print(b)



lr2 = KNeighborsClassifier()

for k, v in b.items():
    if isinstance(v, list):
        setattr(lr2, k, np.array(v))
    else:
        setattr(lr2, k, v)
lr2.predict(X_test[:5])
